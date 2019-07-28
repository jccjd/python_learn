import random
# 名字变大写
list = [{'name':'jam', 'age':15}, {'name':'jam', 'age':15}, {'name':'jam', 'age':15}]
for dict in list:
    dict['name'] = dict['name'].upper()
print(list)
# 1000 个数 20- 100 升序排列， 统计数据重复次数
thousandList = [random.randint(20, 100) for _ in range(1000)]
setList = sorted(set(thousandList))
for i in setList:
    print(i,thousandList.count(i))
