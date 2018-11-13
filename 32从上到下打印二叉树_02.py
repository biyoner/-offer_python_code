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

def layerOrderPrint(root):
    if root:
        dq = deque()
        dq.push(root)
    else:
        return None
    datas = []
    nextNum = 0
    needPrint = 1
    while len(dq.data)>0:
        # q = dq.data[0]
        q = dq.pop()
        datas.append(q.data)
        needPrint -= 1
        if q.left:
            dq.push(q.left)
            nextNum += 1
        if q.right:
            dq.push(q.right)
            nextNum += 1
        # print nextNum,needPrint
        if needPrint == 0:
            print PrintLayer(datas)
            datas = []
            needPrint = nextNum
            nextNum = 0
    return datas

def PrintLayer(l):
    s =""
    if len(l)>0:
        for i in l:
            s = s+ str(i) + " "
    return s


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
    print "Test1"
    layerOrderPrint(tree.root)

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
    print "Test2"
    layerOrderPrint(tree.root)
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
    print "Test3"
    layerOrderPrint(tree.root)

def test4():
    tree = BinaryTree()
    tree.root = Node(1)
    print "Test4"
    layerOrderPrint(tree.root)

def test5():
    tree = BinaryTree()
    print "Test5"
    layerOrderPrint(tree.root)

#        100
#        /
#       50
#         \
#         150
def test6():
    tree = BinaryTree()
    tree.root = Node(100)
    tree.root.left = Node(50)
    tree.root.left.right = Node(150)
    print "Test6"
    layerOrderPrint(tree.root)
if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
