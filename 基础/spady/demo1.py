import re

str = 'dff 1234@qq.com df '
pattern = re.compile(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$')
print(pattern.search(str))