class Array(object):
    def __init__(self, size=32):
        self.size = size
        self._items = [None] * self.size

    def __setitem__(self, key, value):
        self._items[key] = value

    def __getitem__(self, item):
        return self._items[item]


class Queue(object):

    def __init__(self, size=5):
        self.size = size
        self.items = [None] * self.size

        self.head = 0
        self.tail = 0

    def push(self, value):
        self.items[self.head % self.size] = value
        self.head += 1

    def pop(self):
        value = self.items[self.tail % self.size]
        self.tail += 1
        return value


qu = Queue()

qu.push(1)
qu.push(2)
qu.push(3)
qu.push(4)
qu.push(5)
qu.push(6)
print(qu.pop())
print(qu.pop())
print(qu.pop())
print(qu.items)


class Node(object):
    def __init__(self, value=None, _next=None):
        self.value = value
        self.next = _next


class SingList(object):

    def __init__(self):
        node = Node()
        self.root = node
        self.taile = None
        self.length = 0

    def append(self, value):
        node = Node(value)
        if self.taile is None:
            self.root.next = node
        else:
            self.taile.next = node
        self.taile = node
        self.length += 1

    def iter_node(self):
        cur_node = self.root.next
        while cur_node is not None:
            yield cur_node
            cur_node = cur_node.next

    def __iter__(self):
        for cur_node in self.iter_node():
            yield cur_node.value

    def remove(self, value):
        pre_node = self.root
        for cur_node in self.iter_node():
            if cur_node.value == value:
                pre_node.next = cur_node.next
                del cur_node
                self.length += 1
                return
            else:
                pre_node = pre_node.next
        else:
            raise Exception('out of range')

    def reverse(self):
        cur_node = self.root.next
        pre_node = None

        while cur_node:
            cur_next_node = cur_node.next
            cur_node.next = pre_node

            if cur_next_node is None:
                self.root.next = cur_node

            pre_node = cur_node
            cur_node = cur_next_node

def quick(nums, left, right):
    if left > right:
        return nums
    key = nums[left]
    start = left
    end = right

    while left < right:
        while left < right and nums[right] > key:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] < key:
            left += 1
        nums[right] = nums[left]

    nums[left] = key
    quick(nums, start, left - 1)
    quick(nums, left + 1, end)