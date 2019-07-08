##元类实现Singleton
class Singleton(type):
    def __init__(cls,name,base,dict):
        super(Singleton,cls).__init__(name,base,dict)
        cls._instance = None
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton,cls).__call__(*args,**kwargs)
        return cls._instance
#new方法实现Singleton
class Singleton1(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton1,cls).__new__(cls,*args,**kwargs)
        return cls._instance

class myClass( metaclass = Singleton):
    def foo(self):
        print("je")

class myClass1(Singleton1):
    def foo(self):
        pass
if __name__ == '__main__':
    a = myClass1()
    a.foo()
    print(id(a))
    ab= myClass1()
    print(id(ab))
    a = myClass()
    a.foo()
    print(id(a))
    ab= myClass()
    print(id(ab))