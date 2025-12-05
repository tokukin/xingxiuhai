from fastapi import APIRouter, HTTPException
from database_operation import databaseOperation

# 定义化学路由（保留原tags和接口逻辑）
chemical_router = APIRouter(tags=["化学"])

@chemical_router.get("/element/all")
def get_chemical_elements():
    db_op = databaseOperation()
    elements = db_op.get_all_element_base_info()
    if not elements:
        raise HTTPException(status_code=404, detail="元素不存在")
    data = []
    for element in elements:
        data.append({
            "atomic": element[0],
            "symbol": element[1],
            "chinesename": element[2],
            "englishname": element[3],
            "weight": element[4],
            "series": element[5],
            "expandedconfig": element[6],
            "electronstring": element[7],
        })
    length = len(data)
    return {
        "status": 200,
        "message": "获取元素成功",
        "length": length,
        "data": data,
    }

# 后续化学相关接口（如元素详情、化学方程式）可添加在这里