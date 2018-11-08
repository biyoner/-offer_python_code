#coding= utf-8
#author:Biyoner
class BinaryTreeNode(object):
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

def ConnectTreeNodes(node1,node2,node3):
    node1.left = node2
    node1.right = node3

'''构造树的双向链表，返回这个双向链表的最左结点和最右结点的指针'''
def ConvertNode(root):
    if root is None:
        return (None, None)

    # 递归构造出左子树的双向链表
    (l_1, r_1) = ConvertNode(root.left)
    left_most = l_1 if l_1 is not None else root

    (l_2, r_2) = ConvertNode(root.right)
    right_most = r_2 if r_2 is not None else root

    # 将整理好的左右子树和root连接起来
    root.left = r_1
    if r_1 is not None:r_1.right = root
    root.right = l_2
    if l_2 is not None:l_2.left = root
    return (left_most, right_most)
    # 由于是双向链表，返回给上层最左边的结点和最右边的结点指针

def preorder(root):
    if root is None:
        return []
    result = [root.data]
    left_tree = preorder(root.left)
    right_tree = preorder(root.right)
    return result + left_tree +right_tree

def printlist(node):
    datas = []
    while node:
        datas.append(node.data)
        node = node.right
    return datas

#            10
#         /      \
#        6        14
#       /\        /\
#      4  8     12  16
def test1():
    tree = BinaryTree()
    pNode10 = BinaryTreeNode(10)
    pNode6 = BinaryTreeNode(6)
    pNode14 = BinaryTreeNode(14)
    pNode4 = BinaryTreeNode(4)
    pNode8 = BinaryTreeNode(8)
    pNode12 = BinaryTreeNode(12)
    pNode16 = BinaryTreeNode(16)
    tree.root = pNode10
    ConnectTreeNodes(pNode10, pNode6, pNode14)
    ConnectTreeNodes(pNode6, pNode4, pNode8)
    ConnectTreeNodes(pNode14, pNode12, pNode16)
    left_most, right_most = ConvertNode(tree.root)
    print "Test1"
    print printlist(left_most)

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
    pNode5 = BinaryTreeNode(5)
    pNode4 = BinaryTreeNode(4)
    pNode3 = BinaryTreeNode(3)
    pNode2 = BinaryTreeNode(2)
    pNode1 = BinaryTreeNode(1)
    tree.root = pNode5
    ConnectTreeNodes(pNode5, pNode4, None)
    ConnectTreeNodes(pNode4, pNode3, None)
    ConnectTreeNodes(pNode3, pNode2, None)
    ConnectTreeNodes(pNode2, pNode1, None)
    left_most, right_most = ConvertNode(tree.root)
    print "Test2"
    print printlist(left_most)

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
    pNode5 = BinaryTreeNode(5)
    pNode4 = BinaryTreeNode(4)
    pNode3 = BinaryTreeNode(3)
    pNode2 = BinaryTreeNode(2)
    pNode1 = BinaryTreeNode(1)
    tree.root = pNode5
    ConnectTreeNodes(pNode5, None, pNode4)
    ConnectTreeNodes(pNode4, None, pNode3)
    ConnectTreeNodes(pNode3, None, pNode2)
    ConnectTreeNodes(pNode2, None, pNode1)
    left_most, right_most = ConvertNode(tree.root)
    print "Test3"
    print printlist(left_most)

def test4():
    tree = BinaryTree()
    pNode5 = BinaryTreeNode(5)

    tree.root = pNode5
    ConnectTreeNodes(pNode5, None, None)

    left_most, right_most = ConvertNode(tree.root)
    print "Test4"
    print printlist(left_most)

def test5():
    tree = BinaryTree()
    left_most, right_most = ConvertNode(tree.root)
    print "Test5"
    print printlist(left_most)
if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()

