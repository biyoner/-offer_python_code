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

#####Solution1#####
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

def IsBalanced1(root):
    if not root:
        return True
    left = 0
    right = 0
    if root.left:
        left = TreeDepth(root.left)
    if root.right:
        right = TreeDepth(root.right)
    if abs(left-right)<=1:
        return False

    return IsBalanced1(root.left) and IsBalanced1(root.right)

#####Solution2#####
def IsBalanced2(root):
    if not root:
        return 0,True
    left = 0
    right = 0
    fl = True
    fr = True
    if root.left:
        left,fl = IsBalanced2(root.left)
    if root.right:
        right,fr = IsBalanced2(root.right)
    f = False if abs(left-right)>1 else True
    return max(left,right)+1, fl and fr and f

def Test(name,node,expectedValue):
    _,flag = IsBalanced2(node)
    if flag == expectedValue:
        print name + " is passed !"
    else:
        print name + " is failed !"


# 完全二叉树
#             1
#         /      \
#        2        3
#       /\       / \
#      4  5     6   7
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
    ConnectTreeNodes(pNode3, pNode6, pNode7)

    Test("Test1", pNode1, True)

#            1
#         /      \
#        2        3
#       /\         \
#      4  5         6
#        /
#       7
def test2():
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

    Test("Test2", pNode1, True)

# 不是平衡二叉树
#             1
#         /      \
#        2        3
#       /\
#      4  5
#        /
#       6
def test3():
    pNode6 = Node(6)
    pNode5 = Node(5)
    pNode4 = Node(4)
    pNode3 = Node(3)
    pNode2 = Node(2)
    pNode1 = Node(1)
    ConnectTreeNodes(pNode1, pNode2, pNode3)
    ConnectTreeNodes(pNode2, pNode4, pNode5)
    ConnectTreeNodes(pNode5, pNode6, None)

    Test("Test3", pNode1, False)

#               1
#              /
#             2
#            /
#           3
#          /
#         4
#        /
#       5
def test4():

    pNode5 = Node(5)
    pNode4 = Node(4)
    pNode3 = Node(3)
    pNode2 = Node(2)
    pNode1 = Node(1)

    ConnectTreeNodes(pNode1, pNode2, None)
    ConnectTreeNodes(pNode2, pNode3, None)
    ConnectTreeNodes(pNode3, pNode4, None)
    ConnectTreeNodes(pNode4, pNode5, None)

    Test("Test4", pNode1, False)

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
def test5():

    pNode5 = Node(5)
    pNode4 = Node(4)
    pNode3 = Node(3)
    pNode2 = Node(2)
    pNode1 = Node(1)

    ConnectTreeNodes(pNode1, None, pNode2)
    ConnectTreeNodes(pNode2, None, pNode3)
    ConnectTreeNodes(pNode3, None, pNode4)
    ConnectTreeNodes(pNode4, None, pNode5)

    Test("Test5", pNode1, False)

#树中只有1个结点
def test6():
    pNode1 = Node(1)
    Test("Test6", pNode1, True)
#树中没有结点
def test7():
    Test("Test7", None, True)
if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()