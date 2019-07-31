class Array(object):
    def __init__(self, size=32):
        self.size = size
        self.item = [None] * size

    def __setitem__(self, key, value):
        if key > self.size:
            # raise IndexError ('数组越界了')
            newszie = self.size + key
            newarray = [None] * newszie
            for i in range(self.size):
                newarray[i] = self.item[i]
            self.item = newarray
            self.item[key] = value
            self.size = newszie
        else:
            self.item[key] = value

    def __getitem__(self, key):
        return self.item[key]

    def __iter__(self):
        for i in self.item:
            yield i

    def __len__(self):
        return self.size

    def clear(self, value=None):
        for i in range(self.size):
            self.item[i] = value

a = Array(10)
a[0] = 1
a[31] = 1
for i in a:
    print(i)
