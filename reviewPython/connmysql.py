from pymysql import *
conn = connect(
    host='localhost',
    port=3306,
    database='python_test_1',
    user='root',
    password='root',
    charset='utf8'
)

cs1 = conn.cursor()
count = cs1.execute('select * from students')

print(cs1.fetchall())
cs1.close()
conn.close()
