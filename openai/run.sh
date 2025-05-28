# 构建镜像，给它一个名称（例如 microservice-search）
# 后台运行，映射端口，传递环境变量，给容器命名
docker build -t microservice-search . && docker run -d \
  --name microservice-search-app \
  -p 8002:8000 \
  --env-file .env \
  microservice-search
