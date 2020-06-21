"""
生产环境配置
"""
import os

from conf.settings import *

MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = '3306'
MYSQL_USER_NAME = os.environ.get('MYSQL_USER_NAME') or 'an'
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or '123'