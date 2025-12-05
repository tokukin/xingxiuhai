from fastapi import APIRouter

# 定义用户路由（保留原tags和核心配置）
user_router = APIRouter(tags=["用户管理"])

# 后续用户相关接口（如登录、注册）可添加在这里
# 示例：
# @user_router.post("/login")
# def user_login(username: str, password: str):
#     pass