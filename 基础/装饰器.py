'''
装饰任意参数的函数
'''


def deco(func):
    def warpper(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')
    return warpper

@deco
def test():
    print('hell')
test()

def deco(func):
    def warpper(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')
    return warpper

@deco
def myfun1(param1):
    print('run with param %s' % (param1))

@deco
def myfun2(param1, param2):
    print('run with param %s and %s' % (param1, param2))


# myfun1('something')
# myfun2('something','othering')

# 该方式返回的函数名会不同，为此需要functool
from time import time, sleep

def timer(func):
    def warpper(*args, **kwargs):
        tic = time()
        result = func(*args, **kwargs)
        toc = time()
        print(func.__name__)
        return result
    return warpper
@timer
def myfun():
    sleep(2)
    return "end"

# myfun()
# print(myfun.__name__)
import functools

def timer(func):
    @functools.wraps(func)
    def warpper(*args, **kwargs):
        result = func(*args, **kwargs)

        print(func.__name__)
        return result
    return warpper

@timer
def myfun():
    return "end"
myfun()
print(myfun.__name__)














































