class Node(object):
    def __init__(self, data=None):
        self.pre = None
        self.data = data
        self.next = None

class DoubleLinkedlist(object):
    def __init__(self):
        # build root_node and tail_node
        self.root_node = Node()
        self.tail_node = Node()

        # root->next ---> tail
        # tail->pre ---> root
        self.root_node.next = self.tail_node
        self.tail_node.pre = self.root_node
    def append(self,value):

        node = Node(value)
        tail_node = self.tail_node
        pre = tail_node.pre
        pre.next = node
        node.pre = pre
        node.next = self.tail_node
        self.tail_node.pre = node
        return node
    def __len__(self):
        length = 0
        node = self.root_node
        while node.next is not self.tail_node:
            length += 1
            node = node.next
        return length
    def get(self,index):
        node = self.root_node.next
        while index:
            node = node.next
            index -= 1
        return node
    def set(self, index, value):
        node = self.get(index)
        node.data = value
        return node

    def insert(self, index, value):
        index_node = self.get(index)
        pre_node = index_node.pre

        node = Node(value)

        pre_node.next = node
        node.pre = pre_node

        index_node.pre = node
        node.next = index_node
    def delete(self,index):
        node = self.get(index)
        if node:
            node.pre.next = node.next
            node.next.pre = node.pre
            return True
        return False


class MetaClssList(type):
    def __new__(cls, name, base,dct):
        dct = ((k,v) for k,v in dct.items if not k.startwith('__'))
        mapping = dict((k,v) for k,v in dct)

if __name__ == '__main__':
    a = DoubleLinkedlist()
    a.append(1)
    a.set(1,3)
    a.insert(1,2)
    a.delete(1)
    print()

