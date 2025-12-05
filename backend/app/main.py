from typing import Union
from fastapi import FastAPI
import uvicorn
import sys
from fastapi import APIRouter, FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routers.user import user_router
from routers.chemistry import chemical_router
from routers.math import math_router
import os
from dotenv import load_dotenv


load_dotenv()
host = os.getenv("HOST", "127.0.0.1")
port = int(os.getenv("PORT", 8000))
cors_origins = os.getenv("CORS_ORIGINS", "").split(",") if os.getenv("CORS_ORIGINS") else []
title = os.getenv("TITLE", "Science API")
version = os.getenv("VERSION", "1.0.0")

app = FastAPI(title=title, version=version)

# 定义版本路由（添加前缀）
v1_router = APIRouter(prefix="/api/v1")
# 挂载各功能路由到版本路由
v1_router.include_router(user_router, prefix="/users")  # 最终路径：/api/v1/users/*
v1_router.include_router(chemical_router, prefix="/chemical")  # 最终路径：/api/v1/chemical/*
v1_router.include_router(math_router, prefix="/math")  # 最终路径：/api/v1/math/*

app.include_router(v1_router)




app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,  # 允许的源
    allow_credentials=True,  # 允许携带 Cookie
    allow_methods=["*"],  # 允许所有 HTTP 方法（GET、POST、PUT 等）
    allow_headers=["*"],  # 允许所有请求头
)



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    try:
        uvicorn.run(app, host=host, port=port)
    except KeyboardInterrupt:
        print("\nFastAPI服务器正在关闭...")
    finally:
        sys.exit(0)