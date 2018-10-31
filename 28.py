#coding= utf-8
#author:Biyoner
class Node(object):
    def __init__(self,data,left=None,right= None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self):
        self.root = None
    def preOrderLeft(self,root):
        datas = []
        if root:
            datas.append(root.data)
            return datas + self.preOrderLeft(root.left) + self.preOrderLeft(root.right)
        else:
            datas.append(None)
            return datas

    def preOrderRight(self,root):
        datas = []
        if root:
            datas.append(root.data)
            return datas + self.preOrderRight(root.right) + self.preOrderRight(root.left)
        else:
            datas.append(None)
            return datas

def isSymmetry(tree):
    if tree.preOrderLeft(tree.root) == tree.preOrderRight(tree.root):
        return True
    else:
        return False
def Test(name,r, result):
    if r == result:
        print name+" "+"is passed !"
    else:
        print name + " " + "is failed !"

#            8
#        6      6
#       5 7    7 5
def test1():
    tree = BinaryTree()
    tree.root = Node(8)
    tree.root.left = Node(6)
    tree.root.left.left = Node(5)
    tree.root.left.right = Node(7)
    tree.root.right = Node(6)
    tree.root.right.left = Node(7)
    tree.root.right.right = Node(5)
    Test("Test1",isSymmetry(tree),True)

#            8
#        6      9
#       5 7    7 5
def test2():
    tree = BinaryTree()
    tree.root = Node(8)
    tree.root.left = Node(6)
    tree.root.left.left = Node(5)
    tree.root.left.right = Node(7)
    tree.root.right = Node(9)
    tree.root.right.left = Node(7)
    tree.root.right.right = Node(5)
    Test("Test2", isSymmetry(tree), False)

#           8
#        6      6
#       5  7   7
def test3():
    tree = BinaryTree()
    tree.root = Node(8)
    tree.root.left = Node(6)
    tree.root.left.left = Node(5)
    tree.root.left.right = Node(7)
    tree.root.right = Node(6)
    tree.root.right.left = Node(7)
    Test("Test3", isSymmetry(tree), False)


#               5
#              / \
#             3   3
#            /     \
#           4       4
#          /         \
#         2           2
#        /             \
#       1               1
def test4():
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.left.left = Node(2)
    tree.root.left.left.left.left = Node(1)
    tree.root.right = Node(3)
    tree.root.right.right = Node(4)
    tree.root.right.right.right = Node(2)
    tree.root.right.right.right.right = Node(1)
    Test("Test4", isSymmetry(tree), True)

#               5
#              / \
#             3   3
#            /     \
#           4       4
#          /         \
#         6           2
#        /             \
#       1               1
def test5():
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.left.left = Node(6)
    tree.root.left.left.left.left = Node(1)
    tree.root.right = Node(3)
    tree.root.right.right = Node(4)
    tree.root.right.right.right = Node(2)
    tree.root.right.right.right.right = Node(1)
    Test("Test5", isSymmetry(tree), False)


#               5
#              / \
#             3   3
#            /     \
#           4       4
#          /         \
#         2           2
#                      \
#                       1
def test6():
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.left.left = Node(2)
    tree.root.right = Node(3)
    tree.root.right.right = Node(4)
    tree.root.right.right.right = Node(2)
    tree.root.right.right.right.right = Node(1)
    Test("Test6", isSymmetry(tree), False)



def test7():
    tree = BinaryTree()
    tree.root = Node(1)
    Test("Test7", isSymmetry(tree), True)

def test8():
    tree = BinaryTree()
    Test("Test8", isSymmetry(tree), True)


# 所有结点都有相同的值，树对称
#               5
#              / \
#             5   5
#            /     \
#           5       5
#          /         \
#         5           5
def test9():
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(5)
    tree.root.left.left = Node(5)
    tree.root.left.left.left = Node(5)

    tree.root.right = Node(5)
    tree.root.right.right = Node(5)
    tree.root.right.right.right = Node(5)
    Test("Test9", isSymmetry(tree), True)

# 所有结点都有相同的值，树不对称
#               5
#              / \
#             5   5
#            /     \
#           5       5
#          /       /
#         5       5

def test10():
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(5)
    tree.root.left.left = Node(5)
    tree.root.left.left.left = Node(5)

    tree.root.right = Node(5)
    tree.root.right.right = Node(5)
    tree.root.right.right.left = Node(5)
    Test("Test10", isSymmetry(tree), False)

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()


