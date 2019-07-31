# 判断用户输入的字符是否包含空白字符
userstr = 'll'
list = userstr.split(' ')
print(list.__len__() > 1)
def is_has_space(userstr):
    flaglist = userstr.split(' ')
    if len(flaglist) > 1:
        return True
    else:
        return False
# 封装函数 字符串统计 统计字符串中字母数字其他的个数

def getLetter():
    strza = [chr(i) for i in range(65, 91)]
    strAZ = [chr(i) for i in range(97, 123)]

    return  strza + strAZ
def getother():
    other1 = [chr(i) for i in range(33, 48)]
    other2 = [chr(i) for i in range(58, 65)]
    other3 = [chr(i) for i in range(91, 97)]
    other4 = [chr(i) for i in range(123, 127)]

    return other1 + other2 + other3 + other4
def getcount(str):
    number = [f'{i}' for i in range(10)]
    letter = getLetter()
    other = getother()
    numbercount = 0
    lettercount = 0
    othercount = 0

    for i in str:
        if i in number:
            numbercount += 1
        elif i in letter:
            lettercount += 1
        elif i in other:
            othercount += 1
    print(f"number : {numbercount}, letter : {lettercount}, other : {othercount}")



# 去除非字母项fdfd dfsd
def keepletter(str):
    newstr = ''
    letter = getLetter()
    for i in str:
        if i in letter:
            newstr = newstr + i

    return newstr


str ='12131@##~~~~~aaaa'
getcount(str)

newstr = keepletter(str)
print(newstr)

#打印斐波那契数列

fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)


fiblist = [fib(i) for i in range(10)]
print(fiblist)

def fib(n):
    fiblist = []
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        fiblist.append(b)
    return fiblist

fiblist = fib(10)
print(fiblist)
