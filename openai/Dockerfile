# 基础镜像
FROM python:3.11-slim

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装其他 Python 依赖
RUN pip install -r requirements.txt

# 复制应用代码
COPY . .

EXPOSE 8000

# 运行应用（使用 uvicorn 运行） 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]