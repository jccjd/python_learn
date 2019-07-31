class Queue(object):
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.array = [None] * self.maxsize
        self.head = 0
        self.tail = 0

    def __len__(self):
        return self.head - self.tail
    def push(self,value):
        if self.__len__() >= self.maxsize:
            raise Exception('queue is full')
        self.array[self.head % self.maxsize] = value
        self.head += 1
    def pop(self):
        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value

    def __iter__(self):
        for i in self.array:
            yield i

a = Queue(5)
a.push(1)
a.push(2)
a.push(3)
a.push(4)
listd = [i for i in a.__iter__()]
print(listd)
