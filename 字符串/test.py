a = 10
b = 120
if (a is b) :
    print('is false')
if (a is not b):
    print("is true")
# is 与==的区别
# is用于判断两个变量引用对象是否为同一个，==用于判断引用变量的值是否相等
a = [1,2,3]
b = a
print(b is a)
print(b == a)
b = a[:]
print(b)
print(b is a)
print(b == a)


