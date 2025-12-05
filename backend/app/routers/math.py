from fastapi import APIRouter, HTTPException
from database_operation import databaseOperation
from typing import Optional
from math_app.math_util import MathProblemGenerator

# 定义化学路由（保留原tags和接口逻辑）
math_router = APIRouter(tags=["数学"])

@math_router.get("/point")
def get_math_knowledge_points(grade_id: Optional[int] = 0):
    if grade_id > 0 and grade_id <= 24:
        pass
    else:
        grade_id = 0
    db_op = databaseOperation()
    elements = db_op.get_math_knowledge_points(grade_id)
    if not elements:
        return {
        "status": 200,
        "message": "查询失败",
        "grade_id": grade_id,
        "length": 0,
        "data": []
    }
    formatted_data = [
        {"grade_id": item[1],"id": item[0],  "key_point": item[2]} for item in elements
    ]        
    return {
        "status": 200,
        "message": "查询成功",
        "grade_id": grade_id,
        "length": len(formatted_data),
        "data": formatted_data
    }

@math_router.get("/level")
def get_math_calculate_level(grade_id: Optional[int] = 0):
    if grade_id > 0 and grade_id <= 24:
        pass
    else:
        grade_id = 0
    db_op = databaseOperation()
    elements = db_op.get_math_calculate_level(grade_id)
    if not elements:
        return {
        "status": 200,
        "message": "查询失败",
        "grade_id": grade_id,
        "length": 0,
        "data": []
    }
    formatted_data = [
        {"grade_id": item[1],"id": item[0],  "calculate_level": item[2]} for item in elements
    ]        
    return {
        "status": 200,
        "message": "查询成功",
        "grade_id": grade_id,
        "length": len(formatted_data),
        "data": formatted_data
    }


@math_router.get("/problem")
def get_problem(level: Optional[int] = 0):
    """获取指定难度的数学题目"""
    mpg = MathProblemGenerator()
    math_pro = mpg.generate_math_problem(0, level)
    return math_pro
