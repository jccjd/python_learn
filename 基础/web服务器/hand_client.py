class Array(object):
    def __init__(self):
        self.hell = [None]*10

    def __getitem__(self, item):
        return self.hell[item]

    def __setitem__(self, key, value):
        self.hell[key] = value
a = Array()
a[0] = 1
print(a[0])