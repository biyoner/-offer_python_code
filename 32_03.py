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
class stack(object):
    def __init__(self):
        self.data = []
    def pop(self):
        if len(self.data) >0:
            val = self.data[-1]
            self.data.pop()
        else:
            val = None
        return val
    def push(self,val):
        self.data.append(val)

def zhiPrint(root):
    #level1先遍历左，再遍历右
    #level2先遍历右，再遍历左

    level1 = stack()
    level2 = stack()
    if root:
        level2.push(root)
    else:
        return None

    cols = 0
    datas = []
    while len(level1.data) > 0 or len(level2.data) > 0 :
        if cols&1 == 0:
            q = level2.pop()
            datas.append(q.data)
            if len(level2.data) == 0:
                print PrintLayer(datas)
                cols += 1
                datas = []

            if q.left:
                level1.push(q.left)
            if q.right:
                level1.push(q.right)


        else:
            q = level1.pop()
            datas.append(q.data)
            if len(level1.data) == 0:
                print PrintLayer(datas)
                cols += 1
                datas = []
            if q.right:
                level2.push(q.right)
            if q.left:
                level2.push(q.left)


def PrintLayer(l):
    s = ""
    if len(l) > 0:
        for i in l:
            s = s + str(i) + " "
    return s


#            8
#        6      10
#       5 7    9  11
def test1():
    tree = BinaryTree()
    tree.root = Node(8)
    tree.root.left = Node(6)
    tree.root.left.left = Node(5)
    tree.root.left.right = Node(7)
    tree.root.right = Node(10)
    tree.root.right.left = Node(9)
    tree.root.right.right = Node(11)
    print "Test1"
    zhiPrint(tree.root)

#            5
#          4
#        3
#      2
def test2():
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(4)
    tree.root.left.left = Node(3)
    tree.root.left.left.left = Node(2)
    print "Test2"
    zhiPrint(tree.root)
#        5
#         4
#          3
#           2
def test3():
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.right = Node(4)
    tree.root.right.right = Node(3)
    tree.root.right.right.right = Node(2)
    print "Test3"
    zhiPrint(tree.root)

def test4():
    tree = BinaryTree()
    tree.root = Node(5)
    print "Test4"
    zhiPrint(tree.root)

def test5():
    tree = BinaryTree()
    print "Test5"
    zhiPrint(tree.root)

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
    zhiPrint(tree.root)

#                8
#        4              12
#     2     6       10      14
#   1  3  5  7     9 11   13  15
def test7():
    tree = BinaryTree()
    tree.root = Node(8)
    tree.root.left = Node(4)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.left.left = Node(1)
    tree.root.left.left.right = Node(3)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(7)
    tree.root.right = Node(12)
    tree.root.right.left = Node(10)
    tree.root.right.right = Node(14)
    tree.root.right.left.left = Node(9)
    tree.root.right.left.right = Node(11)
    tree.root.right.right.left = Node(13)
    tree.root.right.right.right = Node(15)
    print "Test7"
    zhiPrint(tree.root)
if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
