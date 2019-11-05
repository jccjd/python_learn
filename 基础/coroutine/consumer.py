import time
def consumer():
    resp = ''
    while True:
        n = yield resp
        print('消费者吃了第%d汉堡'%n)
        time.sleep(1)
        resp = '花费200块'

def proudce():
    c.__next__()
    n = 0
    while n < 5:
        n = n + 1
        print('produce-->第{n}个汉堡')
        resp = c.send(n)
        print(resp)
c = consumer()
proudce()