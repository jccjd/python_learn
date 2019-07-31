class Node(object):
    def __init__(self, value=None, pre=None, next=None):
        self.value = value
        self.pre =pre
        self.next = next

class CircleLinkList(object):

    def __init__(self):
        node = Node()
        self.root = node
        self.root.pre = node
        self.root.next = node
        self.length = 0

    def headnode(self):
        return self.root.next

    def __len__(self):
        return self.length

    def tailnode(self):
        return self.root.pre

    def append(self, value):
        node = Node(value)
        tail = self.root.pre
        tail.next = node
        node.pre = tail
        self.root.pre = node
        node.next = self.root
        self.length += 1

    def iter_node(self):
        if self.root.next is self.root:
            return
        flagnode = self.root.next
        while flagnode.next is not self.root:
            yield flagnode
            flagnode = flagnode.next
        yield flagnode

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

    def remove(self, index):
        if index >= 0 and index <= self.length:
            node = self.find(index)
            if node is not self.root and node != -1:
                node.pre.next = node.next
                node.next.pre = node.pre
                del node
                self.length -= 1
            else:
                raise Exception('the linked list is empty')
        else:
            return -1

    def update(self, index, value):
        if index > 0 and index <= self.length:
            node = self.find(index)
            if node is not self.root:
                node.value = value
            else:
                raise Exception('the linked list is empty')
        else:
            return -1


    def iter_node_reverse(self):
        if self.root.pre is self.root:
            return
        curnode = self.root.pre
        while curnode.pre is not self.root:
            yield curnode.pre
            curnode.pre
        yield curnode

# a = CircleLinkList()
# a.append(1)
# a.append(1)
# a.append(1)
# list1 = [i for i in a.__iter__()]
# print(list1)


class Deque(CircleLinkList):

    def pop(self):
        # 删除尾节点
        if len(self) == 0:
            raise Exception('empty')
        tailnode = self.tailnode()
        value = tailnode.value
        self.remove(self.length - 1)
        return value

    def popleft(self):
        if len(self) == 0:
            raise Exception('empty')
        headnode = self.headnode()
        value = headnode.value
        self.remove(0)
        return value
class Testqueue():

    def dpitems(self):
        dp = Deque()
        dp.append(1)
        dp.append(2)
        dp.append(3)
        return dp
    def testpush(self):
        print('-'*10,'test push')
        dp = self.dpitems()
        dp.append(3)
        print(list(dp))
    def testpop(self):
        dp = self.dpitems()
        print('-'*10,'test pop')
        print(list(dp))
        print(dp.pop())
        print(dp.pop())
        print(dp.pop())
    def testpopleft(self):
        dp = self.dpitems()
        print('-'*10,'test popleft')
        print(list(dp))
        print(dp.popleft())
        print(dp.popleft())
        print(dp.popleft())

class Stack(object):
    def __init__(self):
        self.queue = Deque()

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        return self.queue.pop()


testqueue = Testqueue()
testqueue.testpop()
testqueue.testpopleft()