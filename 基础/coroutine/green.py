import time

def consumer():
    r = ''
    while True:
        n = yield r
        print('co')