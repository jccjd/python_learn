# python 数字数据类型用于存储数值数据类型是不允许改变的，这意味着如果改变数字类型的值，将
# 重新分配内存空间
var1 = 1
var2 = 10
# 可以使用del语句删除一些数字对象的引用
del var1,var2
#python支持三种不同的数据类型
#整型（int） 浮点型（float) 复数型（complex)
number = 0xA0F
print(number)
#python数字类型的转换
#在转化时只需将数据类型作为函数名来使用
#int（x)
#float(x)
# complex(x)将x转换到一个复数，实数部分为x，虚数部分为0
# complex(x，y)将x转换到一个复数，实数部分为x，虚数部分为y
a = 1.0
int(a)
print(a)
#python数字运算
print(2 + 2)
print((50 + 5 * 6) / 4) # 20.0
print(8 / 5) #1.6
print(8 // 5) #1.6
#在不同的机器上浮点运算的结果可能会不一样在整数除法中，除法 / 总是返回一个浮点数，要丢弃分数部分用 //
#▄︻┻┳═一不同类型的数混合运算时会将整数转换为浮点数
print(3 * 3.75 / 1.5)

