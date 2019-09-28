#### 常用，命令
    
    新建一个项目：
    开启服务器： py manage.py runserver
    新建一个app：py manage.py startapp polls
    数据库迁移：py manage.py migrate 
    同步数据库：py manage.py makemigrations polls
    进入交互模式：py manage.py shell
    运行测试：py manage.py test polls
    
### 报错
1.mysqlclient的版本不支持

    django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.3 or newer is required; you have 0.7.11 解决方案：    
    
解决： 修改django的源码

liunx下的位置： `/usr/local/lib/python3.6/dist-packages/django/db/backends/mysql/base.py`

    #if version < (1, 3, 3):
    #    raise ImproperlyConfigured("mysqlclient 1.3.3 or newer is required; you have %s" % Database.__version__)

编码错误

    File "/usr/local/python3/lib/python3.7/site-packages/django/db/backends/mysql/operations.py", line 146, in last_executed_query query = query.decode(errors='replace')
    
    AttributeError: 'str' object has no attribute 'decode'    
2.解决： 依然改源码
    
    query = query.decode(errors='replace') 改为 query = query.encode(errors='replace')
    
    
    