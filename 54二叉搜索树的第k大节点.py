# coding= utf-8
# author:Biyoner

class Node(object):
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
def  ConnectTreeNodes(node,nodel,noder):
    if nodel:
        node.left = nodel
    if noder:
        node.right = noder

def KthNode(root,k):
    if not root:
        return -1
    node,_ = KthNodeCore(root,k)

    if not node:
        return -1
    else:
        return node.data

def KthNodeCore(root,k):
    target = None
    if root.left:
        target,k = KthNodeCore(root.left,k)
    if not target:
        if k==1:
            target = root
        k -= 1

    if (not target) and root.right:
        target,k = KthNodeCore(root.right,k)

    return target,k

def Test(name,node,k,expectedNode):
    if KthNode(node,k) == expectedNode:
        print name + " is passed !"
    else:
        print name + " is failed !"

#            8
#        6      10
#       5 7    9  11
def test1():
    pNode8 = Node(8)
    pNode6 = Node(6)
    pNode10 = Node(10)
    pNode5 = Node(5)
    pNode7 = Node(7)
    pNode9 = Node(9)
    pNode11 = Node(11)

    ConnectTreeNodes(pNode8, pNode6, pNode10)
    ConnectTreeNodes(pNode6, pNode5, pNode7)
    ConnectTreeNodes(pNode10, pNode9, pNode11)

    Test("TestA0", pNode8, 0, -1)
    Test("TestA1", pNode8, 1, 5)
    Test("TestA2", pNode8, 2, 6)
    Test("TestA3", pNode8, 3, 7)
    Test("TestA4", pNode8, 4, 8)
    Test("TestA5", pNode8, 5, 9)
    Test("TestA6", pNode8, 6, 10)
    Test("TestA7", pNode8, 7, 11)
    Test("TestA8", pNode8, 8, -1)

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
    pNode5 = Node(5)
    pNode4 = Node(4)
    pNode3 = Node(3)
    pNode2 = Node(2)
    pNode1 = Node(1)
    ConnectTreeNodes(pNode5, pNode4, None)
    ConnectTreeNodes(pNode4, pNode3, None)
    ConnectTreeNodes(pNode3, pNode2, None)
    ConnectTreeNodes(pNode2, pNode1, None)

    Test("TestB0", pNode5, 0, -1)
    Test("TestB1", pNode5, 1, 1)
    Test("TestB2", pNode5, 2, 2)
    Test("TestB3", pNode5, 3, 3)
    Test("TestB4", pNode5, 4, 4)
    Test("TestB5", pNode5, 5, 5)
    Test("TestB6", pNode5, 6, -1)
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
    pNode5 = Node(5)
    pNode4 = Node(4)
    pNode3 = Node(3)
    pNode2 = Node(2)
    pNode1 = Node(1)
    ConnectTreeNodes(pNode1, None, pNode2)
    ConnectTreeNodes(pNode2, None, pNode3)
    ConnectTreeNodes(pNode3, None, pNode4)
    ConnectTreeNodes(pNode4, None, pNode5)

    Test("TestC0", pNode1, 0,  -1)
    Test("TestC1", pNode1, 1,  1)
    Test("TestC2", pNode1, 2, 2)
    Test("TestC3", pNode1, 3,  3)
    Test("TestC4", pNode1, 4, 4)
    Test("TestC5", pNode1, 5, 5)
    Test("TestC6", pNode1, 6, -1)

# There is only one node in a tree
def test4():
    pNode1 = Node(1)
    Test("TestD0", pNode1, 0,  -1)
    Test("TestD1", pNode1, 1, 1)
    Test("TestD2", pNode1, 2,  -1)

# empty tree
def test5():
    Test("TestE0", None, 0, -1)
    Test("TestE1", None, 1, -1)


if __name__ == "__main__":
   test1()
   test2()
   test3()
   test4()
   test5()