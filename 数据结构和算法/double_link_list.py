'''节点类'''


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.pre = None
        self.next = None


class DoubleLinkList(object):
    def __init__(self):
        head = Node()
        tail = Node()
        self.head = head
        self.tail = tail
        self.head.next = self.tail
        self.tail.pre = self.head

    def __len__(self):
        length = 0
        node = self.head
        while node.next is not self.tail:
            length += 1
            node = node.next
        return length

    def append(self, data):
        node = Node(data)
        pre = self.tail.pre
        pre.next = node
        node.pre = pre
        self.tail.pre = node
        node.next = self.tail
        return node

    def get(self, index):

        length = len(self)
        index = index if index >= 0 else length + index
        if index >= length or index < 0: return None
        node = self.head.next
        while index:
            node = node.next
            index -= 1
        return node

    def set(self, index, data):
        node = self.get(index)
        if node:
            node.data = data
        return node

    def insert(self, index, data):

        length = len(self)
        if abs(index + 1) > length:
            return False
        index = index if index >= 0 else index + 1 + length
        next_node = self.get(index)

        if next_node:
            node = Node(data)
            pre_node = next_node.pre
            pre_node.next = node
            node.pre = pre_node
            node.next = next_node
            next_node.pre = node
            return node

    def delete(self, index):
        node = self.get(index)
        if node:
            node.pre.next = node.next
            node.next.pre = node.pre
            return True
        return False


def test_double_link_list():
    a = DoubleLinkList()
    a.append(1)
    a.append(2)
    # get test
    a1value = a.get(0).data
    assert a1value == 1
    # set test
    setdata = a.set(0, 2)
    print(a.head.next.data)


if __name__ == '__main__':
    test_double_link_list()
