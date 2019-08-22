import re
import urllib.request
from gevent import monkey
import gevent
monkey.patch_all()
import random
import requests
context = requests.get("https://movie.douban.com/subject/26909790/celebrities").text


patten = re.compile('class="avatar" style=".*?url\((.*?)\)">')

images = patten.findall(context)
def my_download(url):
    print(url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    with open(f"image/{random.random()}.jpg","wb") as f:
        f.write(data)


for image in images:
    gevent.joinall([
        gevent.spawn(my_download, image)
    ])
