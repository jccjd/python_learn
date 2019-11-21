import pymysql


class MySQL(object):

    def __init__(self, config):
        self._instance = pymysql
        try:
            self.conn = pymysql.connect(
                host='',
                port=3306,
                database='demo',
                user='root',
                password='root',
                charset='utf8'
            )

            self.cursor = self.conn.cursor()
        except pymysql.Error:
            print('mysql error')

    def query(self, sql):
        try:
            self.cursor.execute('SET NAMES utf8')
            result = self.cursor.execute(sql)
        except:
            raise pymysql.Error()
        return result

    def fetchAllRows(self):
        return self.cursor.fetchall()

    def fetchoneRow(self):
        return self.cursor.fetchone()

    def getRowCount(self):
        u"""获取结果行数"""
        return self.cursor.rowcount


    def insert(self, sql):
        try:
            self.cursor.execute('SET NAMES utf8')
            result = self.cursor.execute(sql)
            pk = self.conn.insert_id()
            self.conn.commit()
            return pk
        except:
             raise pymysql.err

    def update(self, sql):
        u"""执行 UPDATE 及 DELETE 语句"""
        try:
            self.cursor.execute("SET NAMES utf8")
            result = self.cursor.execute(sql)
            self.conn.commit()
        except :
            result = False
        return result

    def close(self):
        self.cursor.close()
        self.conn.close()

    def __del__(self):
        u"""释放资源（系统GC自动调用）"""
        try:
            self.cursor.close()
            self.conn.close()
        except:
            pass



if __name__ == '__main__':

    # 数据库连接参数
    dbconfig = {
        'host': '106.53.41.243',
        'port': 3306,
        'user': 'root',
        'passwd': 'root',
        'db': 'demo',
        'charset': 'utf8'
    }
    db = MySQL(dbconfig)

    # 操作数据库
    sql = "select * from user"
    db.query(sql)

    # 获取结果列表
    result = db.fetchAllRows()
    print(result[0])
    for row in result:
        # 使用下标进行取值
        print(row[0])

        # 对列进行循环
        for colum in row:
            print(colum)

    # 关闭数据库
    db.close()
