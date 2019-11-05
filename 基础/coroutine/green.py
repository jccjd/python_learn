import time

def consumer():
    r = ''
    while True:
        n = yield r
        print('消费-->', n)
        time.sleep(1)
        r = '200 ok'

def produce():
    c.__next__()
    n = 0
    while n < 5:
        n = n + 1
        print('produce ---> ', n)
        r = c.send(n)
        print(r)

c = consumer()
produce()

