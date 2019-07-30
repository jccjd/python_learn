class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        node = Node()
        self.root = node
        self.tail = None
        self.length = 0

    def append(self, value):
        node = Node()
        if self.tail is None:
            self.root.next = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1

    def iter_node(self):
        flaginde = self.root.next
        while flaginde.next is not None:
            yield flaginde
            flaginde = flaginde.next
        if flaginde is not None:
            yield flaginde

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def remove(self, index):
        flagindex = 0
        prevnode = self.root
        for node in self.iter_node():
            if flagindex == index:
                prevnode.next = node.next
                del node
                self.length -= 1
                return 1
            flagindex += 1
        return -1

    def find(self, index):
        flagindex = 0
        for node in self.iter_node():
            if flagindex == index:
                return node
            flagindex += 1
        return -1

    def update(self, index, value):
        node = self.find(index)
        if node is not None:
            node.value = value
            return node
        return -1


