import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv


load_dotenv()
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_PORT = int(os.getenv('DATABASE_PORT'))
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_USER = os.getenv('DATABASE_USER')



class databaseOperation:
    def __init__(self):
        self.config = {
        "host": DATABASE_HOST,       # 数据库地址
        "port": DATABASE_PORT,              # 端口
        "user": DATABASE_USER,            # 用户名
        "password": DATABASE_PASSWORD,      # 密码
        # "database": "chemistry",  # 提前创建的数据库名
        "charset": "utf8mb4"       # 字符集（与表结构一致）
    }

    def connect(self):
        try:
            connection = mysql.connector.connect(**self.config)
            if connection.is_connected():
                cursor = connection.cursor()
                print("数据库连接成功")
                return connection, cursor
        except Error as e:
            print(f"数据库连接失败: {e}")
            return None, None
    
    def close(self, connection, cursor):
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("数据库连接已关闭")

    def get_all_element_base_info(self):
        connection, cursor = self.connect()
        if connection and cursor:
            try:
                query = "SELECT el.`atomic`, el.symbol ,el.chinesename ,el.englishname ,el.weight ,el.series ,el.expandedconfig ,el.electronstring FROM chemistry.elements el"
                print(query)
                
                cursor.execute(query)
                results = cursor.fetchall()
                print(f'查询到 {len(results)} 条元素基础信息')
                return results
            except Error as e:
                print(f"查询元素基础信息失败: {e}")
                return None
            finally:
                self.close(connection, cursor)


    def get_math_knowledge_points(self, grade_id: int = 0):
        connection, cursor = self.connect()
        if connection and cursor:
            try:
                query = "SELECT mkp.id,mkp.grade_id ,mkp.key_point  FROM math.math_knowledge_point mkp WHERE mkp.grade_id = %s ORDER BY mkp.id ASC"
                full_sql = query % (grade_id,)  # int类型直接拼接，无需引号
                print(f"执行的完整SQL：{full_sql}")  # 打印最终执行的SQL
                
                cursor.execute(full_sql)
                results = cursor.fetchall()
                print(f'查询到 {len(results)} 条知识点')
                return results
            except Error as e:
                print(f"查询知识点失败: {e}")
                return None
            finally:
                self.close(connection, cursor)
    def get_math_calculate_level(self, grade_id: int = 0):
        connection, cursor = self.connect()
        if connection and cursor:
            try:
                query = "SELECT mcl.id,mcl.grade_id ,mcl.calculate_level  FROM math.math_calculate_level mcl WHERE mcl.grade_id = %s ORDER BY mcl.id ASC"
                full_sql = query % (grade_id,)  # int类型直接拼接，无需引号
                print(f"执行的完整SQL：{full_sql}")  # 打印最终执行的SQL
                
                cursor.execute(full_sql)
                results = cursor.fetchall()
                print(f'查询到 {len(results)} 条口算等级')
                return results
            except Error as e:
                print(f"查询口算等级失败: {e}")
                return None
            finally:
                self.close(connection, cursor)

if __name__ == "__main__":
    db_op = databaseOperation()
    elements = db_op.get_math_knowledge_points(3)
    if elements:
        for element in elements:
            print(element)
        
    



