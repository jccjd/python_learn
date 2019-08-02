class Queue(object):
    def __init__(self):
        self.__list = []

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        return self.__list.pop(0)

    def is_empty(self):
        return self.__list == []

    def __len__(self):
        return len(self.__list)

qu = Queue()
qu.push(1)
qu.push(2)
qu.push(3)
print(qu.pop())
print(qu.pop())
print(qu.pop())