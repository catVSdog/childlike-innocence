"""
开发环境配置
"""
import os

#  flask
import redis

default_secret_key = b'\xf0~<\x1e\xc0\x80\xc8\x1c%X`\xe3\xf7\x98\x9b\xd9'
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or default_secret_key

# mysql

MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = '3306'
MYSQL_USER_NAME = 'an'
MYSQL_PASSWORD = '123'

# sqlalchemy
# ! db must exists in databases
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER_NAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/default'
SQLALCHEMY_BINDS = {
    'blog': f'mysql+pymysql://{MYSQL_USER_NAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/blog',
    'admin': f'mysql+pymysql://{MYSQL_USER_NAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/admin',
}

# session

SESSION_COOKIE_NAME = 'SESSION_ID'
SESSION_TYPE = 'redis'
SESSION_USE_SIGNER = True
SESSION_REDIS = redis.Redis()  # localhost redis, 0 db
PERMANENT_SESSION_LIFETIME = 60 * 60  # 1 hour