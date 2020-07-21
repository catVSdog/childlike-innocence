# childlike-innocence
个人站点后端代码

### 相关命令

1.Flask Migrate 初始化
```
flask db init --multidb
```

2.创建迁移文件
```python
flask db migrate -m "Initial migration."
```

3.迁移数据库
```python
flask db upgrade
```

4.测试`rest_api`
```python
http://localhost:5000/backend_blog/blog/;
http://localhost:5000/backend_blog/blog/10;
```
