class myrange:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            number = self.start
            self.start += 1
            return number
        else:
            raise StopIteration
iters = myrange(90,100)
iters = iter(iters)

list = [1,2,3,4]
iters = iter(list)

while True:
    try:
        print(next(iters))
    except StopIteration:
        break

import time

#生成器
def genrator_fun():
    a = 1
    print('value a')
    yield a
    b = 2
    print('valur b')
    yield b
gen1 = genrator_fun()
print(gen1)
print('*'*20)
print(next(gen1))
print(next(gen1))

def product():
    for i in range(100):
        yield i

produce = product()
print(produce.__next__())

print(produce.__next__())
print(next(produce))

# number = 0
# for i in produce:
#     print(i)
#     number += 1
#     if number == 5:
#
#         break
#
#列表推导式
list = [i for i in range(10)]
# 生成器表达式
list1 = (i for i in range(10))
print(list)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1)
print(next(list1))#next本质就是调用__next__
# <generator object <genexpr> at 0x000001DDB26C5F48>
sum = sum(x ** 2 for x in range(4))
print(sum)