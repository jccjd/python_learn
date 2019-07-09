a = "a"
# print(id(a))#140721507197776
a = "b"
# print(id(a))#140721507197808

a = []
a.append(1)
# print(id(a))#2687715074696
a.append(2)
# print(id(a))#2687715074696




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

a = range(1,10)
print(type(a))
print(a)
