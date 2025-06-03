from pathlib import Path
from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

# 收集所有文件ID
file_ids = []

# 把每个 PDF / MD / TXT 传到向量库
for file in Path("docs").glob("*.*"):
    # 先创建文件
    uploaded_file = client.files.create(
        purpose="assistants",  # 用于助手的文件
        file=open(file, "rb")
    )
    file_ids.append(uploaded_file.id)
    print(f"Uploaded file: {file.name} -> {uploaded_file.id}")

# 将所有文件添加到向量存储
if file_ids:
    vs = client.vector_stores.create(name="services-docs-rag", file_ids=file_ids)

VECTOR_STORE_ID = vs.id
print("Vector store ready:", VECTOR_STORE_ID)
print(f"Added {len(file_ids)} files to vector store")