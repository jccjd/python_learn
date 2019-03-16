num = 100
num2 ="100"
name = 'laowang'
int (num2)
str(num)
print (len(name))
# userNme = input('输入用户名：')
# 字符串加法
a = 'lao'
b = 'wang'
c = 'zhao'
d = a+b
print(d)
#字符串切片
name = 'adcdefABCDEF'
# print(name[2:4]) -->cd
# name[2:-1] cd--E 倒数第二个
# name[2:]
# name[2:-1:2] 跳一个取
#倒序 name[-1:0:-1] name[::-1]
#字符串常见操作
myStr = 'hello world itcast and itcastxxcpp'
print(myStr.find('world'))
print(myStr.count('world'))
#替换 不可对原始值操作
print(myStr.replace('world','wolld'))
print(myStr)
#切割
print(myStr.split(" "))
#第一个大写
print(myStr.capitalize())
#所有第一个大写
print(myStr.title())
#判断以什么开头，以什么结尾 返回true startwidth endwidth
file_name = 'xx.txt'
print(file_name.endswith(".txt"))
#lower 转换字符中所有大写字符为小写 upper
print(myStr.lower())
#find
print(myStr.find('itcast'))
#conut
print(myStr.count('itcast'))
#replace
name = 'hell0 world ha ha'
print(name.replace('ha','Ha'))
print(myStr.partition('itcast'))