def factorial(n):

   if n == 1:
       return 1
   return n *factorial(n - 1)

print(factorial(5))
def fib(n):
    a, b = 0, 1
    listd = []
    for _ in range(n - 1 ):
        a, b = b, a + b
        listd.append(b)
    return listd
print(fib(10))

"""匿名函数"""
a = lambda x : True if x % 2 else False
def decodelambda(n):
    if n % 2 == 0:
        return False
    else:
        return True
print(decodelambda(3))
print(a(3))

"""100以内的3的倍数"""

foo = [i for i in range(101)]
b = filter(lambda x: x % 3 == 0, foo)

for _ in b:
    print(b.__next__())
