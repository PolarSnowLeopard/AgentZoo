from pathlib import Path
from openai import OpenAI
import os
import dotenv
import json
import asyncio
from agents import Agent, Runner
from agents.tool import WebSearchTool, FileSearchTool

dotenv.load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

# 获取向量存储
try:
    stores = client.vector_stores.list(limit=100).data
    vec = next(s for s in stores if s.name=="services-docs-rag")
    VECTOR_STORE_ID = vec.id
except Exception as e:
    print(f"警告: 无法获取向量存储: {e}")
    VECTOR_STORE_ID = None

# --- 本地自定义工具 ---
# @function_tool
# def convert_currency(amount: float, from_code: str, to_code: str) -> float:
#     """离线汇率（演示用，真实场景可连实时 API）"""
#     rates = {"USD": 1.0, "EUR": 0.92, "CNY": 7.1}
#     return round(amount / rates[from_code] * rates[to_code], 2)

# --- OpenAI 内置工具 ---
web_search = WebSearchTool()

# 只有在向量存储可用时才创建file_search工具
tools = [web_search]
if VECTOR_STORE_ID:
    file_search = FileSearchTool(vector_store_ids=[VECTOR_STORE_ID], max_num_results=10)
    tools.append(file_search)

assistant = Agent(
    name="Research-Bot",
    model="gpt-4o",
    instructions=(
        "你是严谨的微服务检索助手："
        "1) 如果有file_search工具，先用它在内部资料里查找用户输入字段含义以及系统已有微服务相关信息；"
        "2) 如涉及领域知识，则调用 web_search；"
        "3) 最终用 json 格式返回微服务名称数组，并给出理由。"
        "4) 请根据用户提供的查询条件，匹配最相关的微服务。"
        "\n"
        "返回结果格式（直接返回json字符串，不要携带```符号）："
        "{"
        "  \"services\": [\"service1\", \"service2\"], "
        "  \"reasoning\": \"根据用户查询条件，匹配到以下微服务：\\n- 微服务1：提供XXX功能\\n- 微服务2：提供YYY功能\\n...\" "
        "}"
    ),
    tools=tools,
)

def construct_user_message(query_dict):
    # 过滤空值
    filled_fields = {k: v for k, v in query_dict.items() if v and str(v).strip()}
    
    if not filled_fields:
        return "请至少填写一个查询条件来搜索微服务。"
    
    user_message = f"""
请根据以下查询条件，帮我找到相关的微服务：

查询条件：
- 名称: {query_dict.get('name', '') or '未填写'}
- 通用描述: {query_dict.get('description', '') or '未填写'}
- 作用: {query_dict.get('role', '') or '未填写'}
- 功能: {query_dict.get('function', '') or '未填写'}
- 技术要求: {query_dict.get('requirement', '') or '未填写'}

请搜索相关信息并返回匹配的微服务名称列表和推荐理由。
"""
    return user_message

def search_microservices(query_dict):
    """搜索微服务的主函数"""
    try:
        user_message = construct_user_message(query_dict)
        
        # 使用同步版本的Runner
        result = Runner.run_sync(assistant, user_message, max_turns=8)
        
        if hasattr(result, 'final_output'):
            return result.final_output
        else:
            return str(result)
            
    except Exception as e:
        error_msg = f"查询失败: {str(e)}"
        print(f"❌ {error_msg}")
        
        # 返回错误的JSON格式
        return json.dumps({
            "services": [],
            "reasoning": error_msg
        }, ensure_ascii=False)
    
# 1️⃣ 改成异步版本
async def search_microservices_async(query_dict: dict):
    user_message = construct_user_message(query_dict)

    try:
        # 直接 await Runner.run
        result = await Runner.run(
            assistant, user_message, max_turns=8
        )
        return getattr(result, "final_output", result)
    except Exception as e:
        return json.dumps({
            "services": [],
            "reasoning": f"查询失败: {e}"
        }, ensure_ascii=False)


# 测试查询
if __name__ == "__main__":
    query1 = {
        "name": "课题一",
        "description": "",
        "role": "",
        "function": "",
        "requirement": ""
    }
    
    result1 = search_microservices(query1)
    print("\n" + "=" * 30)
    print(result1)
    
    # 测试案例2：风险识别
    query2 = {
        "name": "",
        "description": "风险识别和评估",
        "role": "识别金融风险",
        "function": "风险检测",
        "requirement": ""
    }
    
    result2 = search_microservices(query2)
    print("\n" + "=" * 30)
    print(result2)

