from gevent import monkey
import gevent
import urllib.request
monkey.patch_all()





def my_downLoad(url):
    print('GET: %s'%url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    print('{len(data)} bytes received from {url}')

gevent.joinall([
    gevent.spawn(my_downLoad,'http://www.baidu.com/'),
    gevent.spawn(my_downLoad,'http://www.itcast.com/'),
])