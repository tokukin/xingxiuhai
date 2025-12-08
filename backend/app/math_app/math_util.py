from pydantic import BaseModel
from enum import Enum
import random

class MathProblemGenerator:
    def __init__(self):
        pass

    def generate_math_problem(self,problem_id: int, level):
        """根据难度生成数学题目"""
        '''
        1:1-5的加法
        2:1-5的减法
        3:6-10的加法
        4:6-10的减法
        5:20以内的进位加法
        6:一年级上册总复习
        7:20以内的退位减法
        8:100以内的口算加法
        9:100以内的口算减法
        10:一年级下册总复习
        11:1-6表内乘法
        12:1-6表内除法
        13:7-9表内乘法
        14:7-9表内除法
    '''
        if level == 1:
            # 1-5的加法
            a = random.randint(1, 5)
            b = random.randint(0, 5-a)
            operation = random.choice(["+"])
            expression = f"{a} + {b} = "
            answer = a + b
            
        
        elif level == 2:
            # 1-5的减法
            a = random.randint(1, 5)
            b = random.randint(0, a)
            operation = random.choice(["-"])
            expression = f"{a} - {b} = "
            answer = a - b
            
        
        elif level == 3:
            # 6-10的加法
            a = random.randint(0, 10)
            b = random.randint(0, 10-a)
            operation = random.choice(["+"])
            expression = f"{a} + {b} = "
            answer = a + b
                
            
        elif level == 4:
            # 6-10的减法
            a = random.randint(6, 10)
            b = random.randint(0, a)
            operation = random.choice(["-"])
            expression = f"{a} - {b} = "
            answer = a - b
            
        elif level == 5:
            # 20以内的进位加法
            a = random.randint(1, 9)
            b = random.randint(10-a, 9)
            operation = random.choice(["+"])
            expression = f"{a} + {b} = "
            answer = a + b
            
        elif level == 6:
            # 一年级上册总复习
            operation = random.choice(["+", "-"])
            if operation == "+":
                a = random.randint(1, 19)
                b = random.randint(1, 20-a)
                expression = f"{a} + {b} = "
                answer = a + b
            else:
                # 确保减法结果不为负数
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                a, b = max(a, b), min(a, b)
                expression = f"{a} - {b} = "
                answer = a - b
        elif level == 7:
            # 20以内的退位减法
            a = random.randint(10, 19)
            b = random.randint(a-9, a)
            a, b = max(a, b), min(a, b)
            expression = f"{a} - {b} = "
            answer = a - b
        elif level == 8:
            # 100以内的口算加法
            a = random.randint(1, 99)
            b = random.randint(1, 100-a)
            operation = random.choice(["+"])
            expression = f"{a} + {b} = "
            answer = a + b
            
        elif level == 9:
            # 100以内的口算减法
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            operation = random.choice(["-"])
            a, b = max(a, b), min(a, b)
            expression = f"{a} - {b} = "
            answer = a - b
        elif level == 10:
            # 一年级下册总复习
            operation = random.choice(["+", "-"])
            if operation == "+":
                a = random.randint(1, 99)
                b = random.randint(1, 100-a)
                expression = f"{a} + {b} = "
                answer = a + b
            else:
                # 确保减法结果不为负数
                a = random.randint(1, 100)
                b = random.randint(1, 100)
                a, b = max(a, b), min(a, b)
                expression = f"{a} - {b} = "
                answer = a - b
        elif level == 11:
            # 1-6表内乘法
            a = random.randint(1, 6)
            b = random.randint(1, 6)
            operation = random.choice(["×"])
            expression = f"{a} × {b} = "
            answer = a * b
        elif level == 12:
            # 1-6表内除法
            a = random.randint(2, 6)
            b_pos = []
            for i in range(1, a):
                if a % i == 0:
                    b_pos.append(i)
            
            b = random.choice(b_pos)
        
            operation = random.choice(["÷"])
            expression = f"{a} ÷ {b} = "
            answer = a / b
            
        elif level == 13:
            # 7-9表内乘法
            a = random.randint(7, 9)
            b = random.randint(7, 9)
            operation = random.choice(["*"])
            expression = f"{a} × {b} = "
            answer = a * b
        elif level == 14:
            # 7-9表内除法
            a = random.randint(7, 9)
            b_pos = []
            for i in range(1, a):
                if a % i == 0:
                    b_pos.append(i)
            
            b = random.choice(b_pos)
        
            operation = random.choice(["÷"])
            expression = f"{a} ÷ {b} = "
            answer = a / b
            
        
        return {
            "status": 200,
            
            "message": "查询成功",
            "data": {
                
                "expression": expression,
                "answer": answer,
                "difficulty": level
            }
        }
    

    # 存储用户进度（简单内存存储，生产环境应使用数据库）
    
if __name__ == "__main__":
    for j in range(1, 15):
        for i in range(100):
            mpg = MathProblemGenerator()
            math_pro = mpg.generate_math_problem(i, j)
            print(math_pro)
