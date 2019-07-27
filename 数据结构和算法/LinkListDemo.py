class Node(object):
    def __init__(self, value=None, next=None):
        self.value, self.next = value, next
    def __str__(self):
        return f'{self.value}->{self.next}'
class LinkList():
    def __init__(self):
        node = Node()
        self.root = node
        self.tailroot = None
        self.length = 0
    def append(self,value):
        node = Node(value)
        tailroot = self.tailroot
        if tailroot == None:
            self.root.next = node
        else:
            tailroot.next = node
        self.tailroot = node
        self.length += 1
    # 重新迭代方法将 value 生成为可迭代对象
    def __iter__(self):
        for node in self.iter_node():
            yield node.value
    # 遍历节点
    def iter_node(self):
        curnode = self.root.next
        while curnode is not self.tailroot:
            yield curnode
            curnode = not curnode.next
        if curnode is not None:
            yield curnode

    def remove(self,value):
        prevnode = self.root
        for curnode in self.iter_node():
            if curnode.value == value:
                prevnode.next = curnode.next
                if curnode is self.tailroot:
                    self.tailroot = prevnode
                del curnode
                self.length -= 1
                return 1
            else:
                prevnode = curnode
        return -1
    def find(self,value):
        index = 0
        for curnnode in self.iter_node():
            if curnnode.value == value:
                return index
            index += 1
        return -1


a= LinkList()
a.append(1)
a.append(2)
a.append(3)
print(a.root)