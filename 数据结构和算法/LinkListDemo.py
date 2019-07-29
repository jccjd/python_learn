class Node(object):
    def __init__(self, value=None,next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        node = Node()
        self.root = node
        self.tail = None
        self.length = 0

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node(self):
        flagnode = self.root
        while flagnode is not None:
            yield flagnode
            flagnode = flagnode.next
        if flagnode is not None:
            yield flagnode
    def append(self,value):
        node = Node(value)
        tail = self.tail
        if tail is None:
            self.root.next = node
        else:
            tail.next = node
        self.tail = node
        self.length += 1
    def remove(self,index):
        flagindex = 0
        prevnode = self.root
        for node in self.iter_node():
            if flagindex == index:
                prevnode.next = node.next
                del node
                self.length -= 1
            flagindex += 1
        return -1
    def find(self,index):
        flagindex = 0
        for node in self.iter_node():
            if flagindex == index:
                return node
            flagindex += 1
        return -1

    def update(self,index,value):
        node = self.find(index)
        node.value = value
        return node


a = LinkedList()
a.append(1)
a.append(2)
a.append(3)
print(a.find(1).value)
