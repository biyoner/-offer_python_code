# coding= utf-8
# author:Biyoner

class Node(object):
    def __init__(self,data,left=None,right = None):
        self.data = data
        self.left = left
        self.right = right

def  ConnectTreeNodes(node,nodel,noder):
    if nodel:
        node.left = nodel
    if noder:
        node.right = noder

def TreeDepth(root):
    if not root:
        return 0
    left = 0
    right = 0
    if root.left:
        left = TreeDepth(root.left)
    if root.right:
        right = TreeDepth(root.right)

    return max(left,right)+1

def Test(name,node,expectedValue):
    if TreeDepth(node) == expectedValue:
        print name + " is passed !"
    else:
        print name + " is failed !"


#            1
#         /      \
#        2        3
#       /\         \
#      4  5         6
#        /
#       7
def test1():
    pNode7 = Node(7)
    pNode6 = Node(6)
    pNode5 = Node(5)
    pNode4 = Node(4)
    pNode3 = Node(3)
    pNode2 = Node(2)
    pNode1 = Node(1)
    ConnectTreeNodes(pNode1, pNode2, pNode3)
    ConnectTreeNodes(pNode2, pNode4, pNode5)
    ConnectTreeNodes(pNode3, None, pNode6)
    ConnectTreeNodes(pNode5, pNode7, None)
    Test("Test1", pNode1, 4)

#               1
#              /
#             2
#            /
#           3
#          /
#         4
#        /
#       5
def test2():

    pNode5 = Node(5)
    pNode4 = Node(4)
    pNode3 = Node(3)
    pNode2 = Node(2)
    pNode1 = Node(1)

    ConnectTreeNodes(pNode1, pNode2, None)
    ConnectTreeNodes(pNode2, pNode3, None)
    ConnectTreeNodes(pNode3, pNode4, None)
    ConnectTreeNodes(pNode4, pNode5, None)

    Test("Test2", pNode1, 5)

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

    Test("Test3", pNode1, 5)

def test4():
    pNode1 = Node(1)
    Test("Test4", pNode1, 1)
def test5():
    Test("Test5", None, 0)

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()