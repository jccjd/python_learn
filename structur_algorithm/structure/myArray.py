class Array(object):
    def __init__(self, size=32):
        self.size = size
        self._iterm = [None] * self.size

    def __len__(self):
        return self.size

    def __setitem__(self, key, value):
        if key >= self.size:
            newsize = (key + 12)
            newarray = [None] * newsize
            for i in range(self.__len__()):
                newarray[i] = self._iterm[i]
            self._iterm = newarray
            self.size = newsize
            del newarray
        self._iterm[key] = value

    def __getitem__(self, key):
        if key >= 0 and key <= self.size:
            return self._iterm[key]
        return None

    def __iter__(self):
        for i in self._iterm:
            yield i
def testArray():
    a = Array()
    a[0] = 1
    a[32] = 2
    listd = [i for i in a]
    print(listd)
testArray()