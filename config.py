from dotenv import load_dotenv
import os
import pymysql

# 載入環境變數
load_dotenv()

# Flask 會用的 class


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')


# 資料庫連線用
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'port': int(os.getenv('DB_PORT')),
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}
