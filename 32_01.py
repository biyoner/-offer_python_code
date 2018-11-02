#coding= utf-8
#author:Biyoner
class Node(object):
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self):
        self.root = None

class deque(object):
    def __init__(self):
        self.data = []
    def pop(self):
        if len(self.data) >0:
            val = self.data[0]
            self.data = self.data[1:]
        else:
            val = None
        return val
    def push(self,val):
        self.data.append(val)

def layerOrder(root):
    if root:
        dq = deque()
        dq.push(root)
        # q = root
    else:
        return None
    datas = []
    while len(dq.data)>0:
        # q = dq.data[0]
        q = dq.pop()
        datas.append(q.data)
        if q.left:
            dq.push(q.left)
        if q.right:
            dq.push(q.right)
    return datas

def Test(name, val, result):
    if val == result:
        print name+ " " + "is passed !"
    else:
        print name+ " " + "is failed !"

#            10
#         /      \
#        6        14
#       /\        /\
#      4  8     12  16
def test1():
    tree = BinaryTree()
    tree.root = Node(8)
    tree.root.left = Node(6)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(8)
    tree.root.right = Node(14)
    tree.root.right.left = Node(12)
    tree.root.right.right = Node(16)
    Test("Test1", layerOrder(tree.root), [8, 6, 14, 4,8, 12, 16])

#               5
#              /
#             4
#            /
#           3
#          /
#         2
#        /
#       1
def test2():
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(4)
    tree.root.left.left = Node(3)
    tree.root.left.left.left = Node(2)
    tree.root.left.left.left.left = Node(1)
    Test("Test2", layerOrder(tree.root), [5,4,3,2,1])
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
def test3():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.right = Node(2)
    tree.root.right.right = Node(3)
    tree.root.right.right.right = Node(4)
    tree.root.right.right.right.right = Node(5)
    Test("Test3", layerOrder(tree.root), [1,2,3,4,5])

def test4():
    tree = BinaryTree()
    tree.root = Node(1)
    Test("Test4", layerOrder(tree.root), [1])

def test5():
    tree = BinaryTree()
    Test("Test5", layerOrder(tree.root), None)

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()

