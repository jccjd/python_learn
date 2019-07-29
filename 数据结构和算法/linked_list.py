class Node(object):
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
class LinkedList(object):
    # 初始化
    def __init__(self):
        node = Node()
        self.root = node
        self.tail = None
        self.length = 0
    def append(self, value):
        node = Node(value)
        if self.tail is None:
            self.root.next = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1

    def iter_node(self):
        flagnode = self.root.next
        while flagnode is not None:
            yield flagnode
            flagnode = flagnode.next
    def __iter__(self):
        for node in self.iter_node():
            yield node.value
    def find(self, index):
        flagindex = 0
        for node in self.iter_node():
            if flagindex == index:
                return node
            flagindex += 1
        return -1
    def remove(self,index):
        flagenode = 0
        prevnode = self.root
        for node in self.iter_node():
            if flagenode == index:
                prevnode.next = node.next
                del node
                self.length -= 1
                return 1
            flagenode -= 1
        return -1
    def update(self,index,newvalue):
        node = self.find(index)
        node.value = newvalue
        return node


a = LinkedList()
a.append(1)
a.append(2)
a.append(3)
print(a.find(1).value)
a.update(0,10)
print([i for i in a.__iter__()])


