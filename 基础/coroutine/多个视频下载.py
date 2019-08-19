import os

from gevent import monkey
import gevent
import urllib.request
monkey.patch_all()

def my_downLoad(filename, url):
    print('GET: %s'%url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    with open(filename,'wb') as f:
        f.write(data)
    print(filename)
    print(f'{len(data)/(1024*1024)} m received from {url}')

gevent.joinall([
    gevent.spawn(my_downLoad,'1.jpg','https://i0.hdslb.com/bfs/archive/baf5726bcb6ddf7cdffe99ca75a39192a3e8a514.png'),
    gevent.spawn(my_downLoad,'2.jpg','https://i0.hdslb.com/bfs/sycp/creative_img/201908/a42378345e878a4cde2517b3e4eebdca.jpg'),
])
