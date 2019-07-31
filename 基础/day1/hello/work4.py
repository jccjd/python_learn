# 累加和（1,4）（4,1）
# 1+2+3+4，4 + 3 + 2+ 1
def SumNumber(num1,num2):
    if num1 > num2:
        num1, num2 = num2, num1
    list = [list for list in range(num1, num2 + 1)]
    print(list)
    return sum(list)
a = SumNumber(-10,1)
print(a)

#封装乘法表
def multiplicationTable(layer):
    newstr = ""
    for i in range(1, layer+1):
        for j in range(1, i + 1):
            str = "{} * {} = {} ".format(i,j,i*j)
            newstr +=  str
        newstr += '\n'
    return newstr
a = multiplicationTable(10)
print(a)