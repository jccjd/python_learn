from gevent import monkey
import gevent
import urllib.request
monkey.patch_all()

def my_downLoad(filename, url):
    print('GET: %s' % url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    with open(filename, 'wb') as f:
        f.write(data)

    print('{len(data)} bytes received from {url}')

gevent.joinall([
    gevent.spawn(my_downLoad, '1.mp4', 'http://oo52bgdsl.bkt.clouddn.com/05day.mp4'),
])
