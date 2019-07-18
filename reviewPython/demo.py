l1 = [1,2,2,2,4,62,4,65]
l2 = list(set(l1))
l2 = list(sorted(l2))
print(l2)
# 列表推导式
list2 = [i for i in range(20) if i % 3 is 0]
print(list2)