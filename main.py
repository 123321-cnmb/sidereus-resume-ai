import sys
import os
import json

# 强行将当前根目录加入系统路径，确保云端运行时能正确找到 api、core、services 等文件夹
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from a2wsgi import ASGIMiddleware

# 导入路由模块
from api.routes import router

app = FastAPI(title="Sidereus AI Resume Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 挂载路由
app.include_router(router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Layered Architecture Backend is Working!"}

# 阿里云 FC 适配器
wsgi_app = ASGIMiddleware(app)

def handler(environ, start_response):
    try:
        return wsgi_app(environ, start_response)
    except Exception as e:
        status = '200 OK'
        headers = [('Content-type', 'application/json')]
        start_response(status, headers)
        return [json.dumps({"bridge_error": str(e)}).encode('utf-8')]