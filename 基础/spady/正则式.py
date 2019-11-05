import re
import requests

content = 'Hello 1234567 is a number. Regex String'

pattern = re.compile("^Hello (\d+).*String$")
pattern1 = re.compile(".*(\d+).*")
# 非贪婪
pattern2 = re.compile(".*?(\d+).*",re.S)
print(pattern2.findall(content))

# 多行匹配
content1 = '''Hello is a number. 
           Regex String 1234567'''  # 把数字换到第二行
pattern3 = re.compile(".*?(\d+).*", re.S)
print(pattern3.findall(content1))

# 取出html中的歌手名和歌名
html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''
pattern4 = re.compile('<a.*? singer="(.*?)">(.*?)</a>')
print(pattern4.findall(html))

content = requests.get('https://movie.douban.com/chart').text

with open('douban.html','w+') as f:
    f.write(content)
# 豆瓣电影排行榜
# pattern = re.compile('class="pl2".*?<.*?="(.*?)".*?>(.*?)<span.*?>(.*?)</span>.*?"rating_nums">(.*?)</span>.*?"pl">(.*?)</span>', re.S)
# # compile可以在多次使用中提高效率，这里影响不大
# results = re.findall(pattern, content)
# for result in results:
#     url, name1, name2, nums, pl = result
#     print(url, name1.replace("/","").strip(), name2.replace("/","").strip(), nums, pl)


pattern = re.compile('class="clearfix".*?<.*?>(.*?)</div>.*?<a.*?href="(.*?)".*?>(.*?)</a>',re.S)
results = re.findall(pattern, content)
for result in results:
    top, url, name = result
    with open('topmove.txt','a+') as f:
        f.write("{top} {url} {(re.sub('n', '', name)).strip()} \n")

    # print(top, url, re.sub('\n', " ", name))