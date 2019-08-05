
class A:
    pass

a = A()
print('a对象所在的内存地址是 %d， A类所在的内存地址是 %d' % (id(a), id(A)))
b = A()
print('b对象所在的内存地址是 %d, A类所在的内存地址是 %d' % (id(b), id(A)))
c = A()
print('c对象所在的内存地址是 %d, A类所在的内存地址是 %d' % (id(c), id(A)))


class B(object):
    instant = None
    flag = True

    def __new__(cls, *args, **kwargs):
        if cls.instant is None:
            cls.instant = super().__new__(cls)
        return cls.instant

    def __init__(self):
        self.name = '张三'
d = B()
print('d对象所在的内存地址是 %d, B类所在的内存地址是 %d' % (id(d), id(B)))
e = B()
print('e对象所在的内存地址是 %d, B类所在的内存地址是 %d' % (id(e), id(B)))
f = B()
print('f对象所在的内存地址是 %d, B类所在的内存地址是 %d' % (id(f), id(B)))


class Singleton(type):

    def __init__(cls, name, bases, dct):
        super(Singleton, cls).__init__(name, bases, dct)
        cls._instance = None
    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kw)
        return cls._instance

class MyClass3(metaclass = Singleton):
    def foo(self):
        pass

one = MyClass3()
print(id(one))
two = MyClass3()
print(id(two))

