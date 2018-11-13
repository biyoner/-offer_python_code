#coding= utf-8
#author:Biyoner
import copy

class Node(object):
    def __init__(self, data, left= None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self):
        self.root = None

def FindPath(root, num):
    if not root:
        return None
    lroot = []
    findpath(root,[],num,lroot)
    return lroot

def findpath(root, sum, num, allroot):
    sum.append(root.data)

    if (not root.left) and (not root.right):
        if ALL(sum) == num:
            allroot.append(copy.copy(sum))
        sum.pop()
        return

    if root.left:
        findpath(root.left, sum, num, allroot)
    if root.right:
        findpath(root.right,sum,num,allroot)
    sum.pop()

def ALL(l):
    sum  = 0
    for i in range(len(l)):
       sum += l[i]
    return sum


def Test(name, val, result):
    if val == result:
        print name+ " " + "is passed !"
    else:
        print name+ " " + "is failed !"

#            10
#         /      \
#        5        12
#       /\
#      4  7
def test1():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(5)
    tree.root.right = Node(12)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(7)
    Test("Test1",FindPath(tree.root, 22),[[10,5,7],[10,12]])

#            10
#         /      \
#        5        12
#       /\
#      4  7
# 没有路径上的结点和为15
def test2():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(5)
    tree.root.right = Node(12)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(7)
    Test("Test2",FindPath(tree.root, 15),[])

#               5
#              /
#             4
#            /
#           3
#          /
#         2
#        /
#       1
def test3():
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(4)
    tree.root.left.left = Node(3)
    tree.root.left.left.left = Node(2)
    tree.root.left.left.left.left = Node(1)
    Test("Test3",FindPath(tree.root, 15),[[5,4,3,2,1]])

def test4():
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.right = Node(4)
    tree.root.right.right = Node(3)
    tree.root.right.right.right = Node(2)
    tree.root.right.right.right.right= Node(1)
    Test("Test4",FindPath(tree.root, 16),[])

def test5():
    tree = BinaryTree()
    tree.root = Node(5)
    Test("Test5", FindPath(tree.root, 5), [[5]])

def test6():
    tree = BinaryTree()
    Test("Test6", FindPath(tree.root, 5), None)

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()

