# create database heima
# CREATE TABLE IF NOT EXISTS `goods`(
#    `id` INT UNSIGNED AUTO_INCREMENT,
#    `name` VARCHAR(100) ,
#    `price` decimal(7, 2) NOT NULL,
#    PRIMARY KEY ( `id` )
# )ENGINE=InnoDB DEFAULT CHARSET=utf8;

from pymysql import *
class connect_mysql():
    def connect(self):
        self.conn = connect(
                host='localhost',
                port=3306,
                database='demo',
                user='root',
                password='root',
                charset='utf8'
            )
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_all(self, sql, params=()):
        list = ()
        try:
            self.connect()
            self.cursor.execute(sql, params)
            list = self.cursor.fetchall()
            self.close()
        except :
            print('error')
        return list

    def insert(self, sql, params=()):
        return self.__edit(sql, params)

    def __edit(self, sql, params):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except :
            print('error')

        return count

    def get_one(self, sql, params=()):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
        except:
            print('error')
        return result

orm = connect_mysql()
sql = 'select * from goods where name=%s'
pams = 'n'
have_one = orm.get_one(sql, pams)
print(have_one)


def client():
    orm = connect_mysql()

    print('------商品管理系统---------')
    print('1.添加商品')
    print('2.查询商品')
    while True:
        number = input("请输入序号：")
        if number == 1:
            name = input("请输入输入商品名称：")
            price = input("请输入输入商品单价")
            sql = 'select * from goods where nam=%s'
            have_one = orm.get_one(sql,name)

            if have_one is None:
                sql = 'insert into goods(name,price) values(%s,%s)'
                params=(name, price)

                orm.insert(sql, params)
            else:
                print('名字重复')
        if number == 2:
            number1 = input('输入价格范围1')
            number2 = input('输入价格范围2')
            sql = 'select * from goods where price between %s and %s'
            par=(number1, number2)
            orm.get_one(sql,par)



