from servicesSearchAgent import search_microservices_async
from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI(title="服务智能检索API",
              description="服务智能检索API",
              version="1.0.0")

class SearchRequest(BaseModel):
    name: str | None = ""
    description: str | None = ""
    role: str | None = ""
    function: str | None = ""
    requirement: str | None = ""

@app.get("/health")
def health():
    return {"message": "ok"}

@app.post("/search")
async def search(request: SearchRequest):
    request_dict = request.model_dump()

    # ✅ 直接 await
    raw_result = await search_microservices_async(request_dict)

    try:
        # raw_result是个字典
        parsed = raw_result
    except json.JSONDecodeError:
        parsed = {"raw_output": str(raw_result)}

    return {"success": True, "data": parsed, "query": request_dict}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
