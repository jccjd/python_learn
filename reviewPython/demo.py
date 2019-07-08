a = "a"
print(id(a))#140721507197776
a = "b"
print(id(a))#140721507197808

a = []
a.append(1)
print(id(a))#2687715074696
a.append(2)
print(a)
#单例模式
class Singleton(type):
    def __init__(cls,name,base,dict):
        super(Singleton,cls).__init__(name,base, dict)
        cls._instance = None
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton,cls).__call__(*args, **kwargs)
        return cls._instance
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls._instance


class MyClass3(metaclass = Singleton):
    def foo(self):
        pass


def foo(x):
    print("executing foo(%s)"%(1))
class A(object):
    def foo(self,x):
        print("executing foo(%s,%s)"%(self,x))
    @classmethod
    def class_foo(cls,x):
        print("executing class_foo(%s,%s)"%(cls,x))
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)"%x)

if __name__ == '__main__':

    one = MyClass3()
    print(id(one))
    two = MyClass3()
    print(id(two))
    foo(1)
    a = A()
    a.foo(1)
    A.class_foo(1)
