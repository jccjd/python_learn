import re

str = '1234@qq.com'

pattern1 = re.compile(r'^(\w{2,11})@qq.com')
print(pattern1.findall(str))