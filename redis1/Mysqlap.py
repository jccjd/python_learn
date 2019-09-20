# -*-coding:utf-8-*-
'''
是对 mysqlwapper 的进一步封装
'''
from redis1 import Singleton
from redis1.MySQL import MySQL
from redis1 import configs


class MySQLApp():
    '''派生自己的app数据库类'''
    __metaclass__ = Singleton

    ## 声明一个静态的方法
    @classmethod
    def getInstance(self):
        return MySQL(configs.configs_default['db'])


if __name__ == '__main__':
    Instance = MySQLApp.getInstance()
    sql = 'select * from goods'
    Instance.query(sql)
    print(list(Instance.fetchoneRow()))
