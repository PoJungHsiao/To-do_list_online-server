# 建立資料庫(初始化)
import pymysql
from config import db_config

# 連線到剛建立的資料庫
with pymysql.connect(**db_config) as conn, conn.cursor() as cursor:
    # 建立使用者資料表
    sql = '''CREATE TABLE IF NOT EXISTS USER (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password BLOB NOT NULL,
    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT FALSE)'''
    cursor.execute(sql)
    print("✅ 使用者資料表建立成功(或已存在)")

    # 建立Todo資料表
    sql = '''CREATE TABLE IF NOT EXISTS TODO (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150),
    description VARCHAR(255),
    completed BOOLEAN DEFAULT FALSE,
    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES USER(id))'''
    cursor.execute(sql)
    print("✅ 代辦資料表建立成功(或已存在)")

    conn.commit()
