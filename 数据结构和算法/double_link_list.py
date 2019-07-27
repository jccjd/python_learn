class Node(object):
    def __init__(self, value = None, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next


class CycleDoubleLinkList(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        # 初始化首节点
        node = Node
        node.next = node
        node.prev = node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        node = Node(value)
        tailnode = self.root or self.tailnode()
        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1


a = CycleDoubleLinkList(10)

a.append(1)
a.append(2)
print(a.root.next)
