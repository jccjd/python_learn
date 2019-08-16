import time
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print(f'consuming-->{n}')
        time.sleep(1)
        r = '200$ ok'

def produce():
    c.__next__()
    n = 0
    while n < 5:
        n = n + 1
        print(f'produce-->{n}')
        r = c.send(n)
        print(f'consumer-->{r}')
    pass

c = consumer()
produce()