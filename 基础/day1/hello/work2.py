import random
'''
规则红球： 6个 1-36随机数
蓝球： 1个 1-12 随机数

'''

# 有bug 去重时会少一个球
# print(f'red ball is: {sorted(set([random.randint(1,36) for _ in range(6)]))}\nbule ball is: {[random.randint(1,12)]}')

def doubleBalls():
    while True:
        redBall = set([random.randint(1,36) for _ in range(6)])
        if redBall.__len__() == 6:
            return sorted(redBall),[random.randint(1, 12)]

red, blue = doubleBalls()
print(red, blue)

'''
获取当前文件名的后缀
'''
file1 = 'hello'
file2 = 'hello.txt'
suffix = file2.split('.')
if suffix.__len__() == 1:
    print('该文件无后缀')
else:
    print("文件后缀为:",suffix[1])