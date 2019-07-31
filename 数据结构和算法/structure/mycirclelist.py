class Node(object):
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class CircleList(object):
    def __init__(self):
        node = Node()
        self.root = node
        self.root.prev = node
        self.root.next = node
        self.length = 0

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def iter_node(self):
        flagenode = self.root.next
        while flagenode.next is not self.root:
            yield flagenode
            flagenode = flagenode.next
        yield flagenode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def append(self, value):
        node = Node(value)
        tailnode = self.tailnode()
        tailnode.next = node
        node.prev = tailnode

        self.root.prev = node
        node.next = self.root
        self.length += 1

    def find(self, index):
        flagindex = 0
        if index >=0 and index <= self.length - 1:
            for node in self.iter_node():
                if flagindex == index:
                    return node
                flagindex += 1
        else:
            raise Exception('out of range')

    def remove(self, index):
        node = self.find(index)
        if node is not self.root:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
            del node
        else:
            raise Exception('list is empty')

    def update(self, index, value):
        node = self.find(index)
        if node is not self.root:
            node.value = value
        else:
            raise Exception('list is empty')

    def reverse(self):
        tailnode = self.tailnode()
        while tailnode.prev is not self.root:
            yield tailnode.value
            tailnode = tailnode.prev
        yield tailnode.value
a = CircleList()
a.append(1)
a.append(2)
a.append(3)
# print(a.find(2).value)
# a.remove(0)
# a.update(1, 9)
# listd = [i for i in a]
# a.reverse()
relist = [i for i in a.reverse()]

# print(listd)
print(relist)

