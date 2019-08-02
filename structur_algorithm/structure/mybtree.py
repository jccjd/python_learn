class Node(object):
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return

        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)

            if cur_node.rchild is None:
                cur_node.rchild = node
                return

            else:
                queue.append(cur_node.rchild)


    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item, end=' ')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
    def preoder(self, node):
        """先序遍历"""
        if node is None:
            return
        print(node.item,end=' ')
        self.preoder(node.lchild)
        self.preoder(node.rchild)

    def inoder(self, node):
        if node is None:
            return
        self.inoder(node.lchild)
        print(node.item,end=' ')
        self.inoder(node.rchild)

    def afteroder(self, node):
        if node is None:
            return
        self.afteroder(node.lchild)
        self.afteroder(node.rchild)
        print(node.item,end=' ')
tree = Tree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.breadth_travel()
print('广度优先')

tree.preoder(tree.root)
print('先序')
tree.inoder(tree.root)
print('中序')
tree.afteroder(tree.root)
print('后序')