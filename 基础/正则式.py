import re

print(re.match('www', 'www.baidu.com').span()) # 在起始位置开始
print(re.match('bai','www.baidu.com'))
line = 'Cats are smarter than dogs'
matchObj = re.match(r'(.*) are (.*?) .*',line, )
print('--',matchObj.groups())
if matchObj:
    print("matchObj,group()", matchObj.group())
    print("matchObj,group()", matchObj.group(1))
    print("matchObj,group()", matchObj.group(2))

# search

print(re.search('www', 'www.runoob').span())
print(re.search('com','www.runoob.com').span())
line = "cats are smarter than dogs "
searchObj = re.search(r'(.*) are (.*?) .*', line)
if searchObj:
    print("searchObj.group()", searchObj.group())
    print(searchObj.group(1))
    print(searchObj.group(2))


phone = '2004-959-559 # 这是一个电话号码'

# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码：", num)
# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print(num)
# 参数是个函数
def double(mathed):
    value = int(mathed.group('value'))
    return str(value * 2)
s = 'A23G4H567'
print(re.sub('(?P<value>\d+)', double,s))

# complie(pattern[,flags ,re.I 忽略大小写 re.M多行模式])
pattern = re.compile(r'\d+') # 匹配至少一个数字
m = pattern.match('one12twothree34four')
print(m)
m = pattern.match('one12twothree34four', 3, 10)
print(m)
print(m.group(0))
print(m.start(0))
print(m.end(0))
print(m.span(0))


patttern = re.compile(r'\d+') # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456',0,10)
print(result1)
print(result2)

print(re.split(' ', 'runoob, runoob, runoob'))
print(re.split(' ','this isa b c'))


# 字符匹配
list = 'python Python rube'
pattern = re.compile('[Pp]ython')
print(pattern.findall(list))



word = "123 24"
rulu = re.compile(r'\d+')
print(rulu.findall(word))
