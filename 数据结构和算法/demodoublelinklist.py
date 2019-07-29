class Node(object):
    def __init__(self,value=None,prev=None,next=None):
        self.prev = prev
        self.value = value
        self.next = next
class CircleLinkedList(object):
    def __init__(self):
        node = Node()
        self.root = node
        self.root.prev = node
        self.root.next = node
        self.length = 0

    # 循环链表，tail即使sele.root.pre
    def append(self,value):
        node = Node(value)
        tail = self.root.prev

        tail.next = node
        node.prev = tail

        self.root.prev = node
        node.next = self.root
        self.length += 1

    def iter_node(self):
        if self.root.next is self.root:
            return
        flagindex = self.root.next
        while flagindex.next is not self.root:
            yield flagindex
            flagindex = flagindex.next
        yield flagindex
    def __iter__(self):
        for node in self.iter_node():
            yield node.value
    def find(self,index):
        flagindex = 0
        for node in self.iter_node():
            if flagindex == index:
                return node
            flagindex += 1
        return -1
    def remove(self,index):
        node = self.find(index)
        prevnode = node.prev
        nextnode = node.next
        prevnode.next = nextnode
        nextnode.prev = prevnode
        del node

    def iter_reverse_node(self):
        curnode = self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode
a = CircleLinkedList()
a.append(1)
a.append(2)
a.append(3)
nodevalue = [i for i in a.__iter__()]
reverse = a.iter_reverse_node()
reverselist = [i.value for i in reverse.__iter__()]
print(nodevalue)
print(reverselist)
