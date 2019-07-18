a = "a"
# print(id(a))#140721507197776
a = "b"
# print(id(a))#140721507197808

a = []
a.append(1)
# print(id(a))#2687715074696
a.append(2)
# print(id(a))#2687715074696
#函数调用问题，普通方法不能直接类名调用
#静态方法和类方法可以直接类名访问
class A(object):
    def foo(self):
        print("executing foo()")
    @classmethod
    def class_foo(cls,x):
        print("executing class_foo(%s,%s)"%(cls,x))
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)"%x)

a = A()
# A.foo()#不能使用
A.class_foo(2)
A.static_foo(1)
#*args可以使用任意数量的参数 **kwagrs允许使用事先未定义的参数名
def print_everything(*args,**kwargs):
        print(args,kwargs)
print_everything('dfd','dfdf',cas = 'dsd')

def kwargs_print(**kwargs):
    for name,value in kwargs.items():
        print('{0},{1}'.format(name,value))
kwargs_print(app = 'ling',link = 'fdjf')
