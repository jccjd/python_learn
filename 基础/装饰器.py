def makeBlod(fn):
    def waro():
        return "<b>"+ fn() +"<b>"
    return waro

def makeItero(fn):
    def add():
        return "<i>" + fn() + "<i>"
    return add
@makeBlod
def test1():
    return ('hello1')

@makeItero
def test2():
    return ('hello2')


print(test1())
print(test2())


# 无参数函数
def test(func):
    def wall():
        print(f'{func.__name__}')
        func()
    return wall


@test
def fun():
    print('hello')

fun()

# 装饰器有参数
def timefun(fun):
    def waper(*args,**kwargs):
        print('----waper---')
        print(*args,**kwargs)
        fun(*args, **kwargs)
    return waper


@timefun
def hwlo(a, b):
    print(a + b)

hwlo(1, 2)
import time
hwlo(2, 4)
# 不定长参数
from time import ctime, sleep

def timefun(func):
    def wrappedfunc():
        print("%s called at %s"%(func.__name__, ctime()))
        return func()
    return wrappedfunc

@timefun
def foo():
    print("I am foo")

@timefun
def getInfo():
    return '----hahah---'

foo()
sleep(2)
foo()


print(getInfo())


def demo2(pre='hwllo'):
    def q1(func):
        def q2():
            print(pre)
            return func()
        return q2
    return q1

@demo2('www')
def w2():
    return 'eee'

print(w2())

# 类装饰器
class Test():
    def __init__(self, func):

        print('初始化')
        self.__func = func
    def __call__(self, *args, **kwargs):
        print("初始化中")
        self.__func()
@Test
def test10():
    print('test10')

test10()


class Money(object):
    def __init__(self):
        self.__money = 0

    def getmoney(self):
        return self.__money

    def setmoney(self, value):
        self.__money = value

    money = property(getmoney, setmoney)

class Money1(object):
    def __init__(self):
        self.__money = 0

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print('not int type')

m = Money1()
m.money = 'dd'
print(m.money)

