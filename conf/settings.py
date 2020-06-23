"""
开发环境配置
"""
import os

#  flask 相关配置

default_secret_key = b'\xf0~<\x1e\xc0\x80\xc8\x1c%X`\xe3\xf7\x98\x9b\xd9'
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or default_secret_key

# mysql 相关配置

MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = '3306'
MYSQL_USER_NAME = 'an'
MYSQL_PASSWORD = '123'

# sqlalchemy 相关配置

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER_NAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/default'
SQLALCHEMY_BINDS = {
    'blog': f'mysql+pymysql://{MYSQL_USER_NAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/blogs_db',
}
