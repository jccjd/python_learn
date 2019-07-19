# for i in range(1,10):
#     for j in range(1,i+1):
#         # print(f'{j} * {i} = {i*j} ',end='')
#     # print('')

l1 = [1,2,2,2,4,62,4,65]
l2 = list(set(l1))
l2 = list(sorted(l2))
print(l2)
# 列表推导式
list2 = [i for i in range(20) if i % 3 is 0]
print(list2)
def squared(x):
    return x*x
list2 = [squared(x) for x in range(20) if x%2 is 0]
#生成器推导式
generator = (i ** 2 for i in range(10) if i % 2 is 0)
print(generator)
#字典推导式
#提取字典中的小写key和其内容
mycase = {'a':10,'b':34,'B': 90,'A':10,}
mycase_frequency = {
    k.lower():mycase.get(k.lower()) for k in mycase.keys()
}
mycase_upper = {
    k:mycase.get(k) for k in mycase.keys() if k < 'Z'
}
#合并两个有序列表
def link_two_list(l1,l2,tmp):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return link_two_list(l1,l2,tmp)
def pop_link_list(l1,l2):
    tmp = []
    while l1 and l2:
        if l1[0] < l2[0]:
            tmp.append(l1.pop(0))
        else:
            tmp.append(l2.pop(0))
    while l1:
        tmp.append(l1.pop(0))
    while l2:
        tmp.append(l2.pop(0))
    return tmp

list1 = [1,2,3]
list3 = [3,4,5,5,6]
print(pop_link_list(list1,list3))

def choose(foo):
    if foo == 'foo':
        class foo(object):
            pass
        return foo
    else:
        class boo(object):
            pass
        return boo
foo = type('foo',(),{'bl':10})
print(type(foo))

class demo():
    pass
print(type(demo))
name = dict()
name.items()