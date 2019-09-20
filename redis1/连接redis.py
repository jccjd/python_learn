import redis

from redis1 import Mysqlap
from redis1.MySQL import MySQL
from redis1.Mysqlap import MySQLApp

try:

    r = redis.StrictRedis(host='localhost', port=6379)
except Exception:
    print(Exception)

r.set('name', 'hello')
pipe = r.pipeline()
pipe.set('name', 'world')
pipe.get('name')
pipe.execute()

class RedisHelper():
    def __init__(self, host='localhost', port= 6379):
        self.__redis = redis.StrictRedis(host, port)

    def get(self, key):
        if self.__redis.exists(key):
            return self.__redis.get(key)

    def set(self, key, value):
        self.__redis.set(key, value)

import hashlib

name = 'hell0'
pwd = '10.00'

try:
    redis = RedisHelper()
    if redis.get('name') == name:
        print('ok')
    else:
        db = MySQLApp.getInstance()

        upwd = db.query("select name, price from goods where name='%s'" % name)
        al = db.fetchAllRows()
        bl = al[0][1]
        print(str(bl) == pwd)

        if upwd == 0:
            print('用户名错误')
        elif str(al[0][1]) == pwd:
            redis.set('uname', name)
            print('登陆成功')
        else:
            print('pwd error')
except:

    raise Exception
