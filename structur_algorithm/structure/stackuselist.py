class Stack(object):
    def __init__(self):
        self.__list = []

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        return self.__list.pop()

    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        return self.__list == []

    def __len__(self):
        return len(self.__list)

stack = Stack()
stack.push(0)
stack.push(1)
stack.push(2)
for _ in range(stack.__len__()):
    print(stack.pop())