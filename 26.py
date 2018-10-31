#coding=utf-8
#author: Biyoner

class Node(object):
    def __init__(self,data, left=None, right= None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self):
        self.root = None


def SubTree(root,subtree):
    if (not root) or (not subtree):
        return False
    val = subtree.data
    flag = False
    if root.data == val:
        if isAhasB(root,subtree):
            return True
    if root.left or root.right:
        flag = SubTree(root.left, subtree) or SubTree(root.right,subtree)
    return flag


def isAhasB(r, r_sub):
    flag = False
    if (not r) or (not r_sub):
        return True
    if r.data != r_sub.data:
        return False
    if r.data == r_sub.data:
        flag = (isAhasB(r.left, r_sub.left)) and (isAhasB(r.right, r_sub.right))
        return flag

def Test(name,result,true):
    if result == true:
        print name+" "+"is passed !"
    else:
        print name + " " + "is failed !"

def test1():
# 树中结点含有分叉，树B是树A的子结构
#                  8                8
#              /       \           / \
#             8         7         9   2
#           /   \
#          9     2
#               / \
#              4   7
    tree = BinaryTree()
    tree.root = Node(8)
    second1 = tree.root.left = Node(8)
    second2 = tree.root.right = Node(7)
    third1 = second1.left = Node(9)
    third2 = second1.right = Node(2)
    third2.left = Node(4)
    third2.right = Node(7)

    sub_tree = BinaryTree()
    sub_tree.root = Node(8)
    sub_tree.root.left = Node(9)
    sub_tree.root.right = Node(2)
    result = SubTree(tree.root,sub_tree.root)
    Test("Test1",result,True)

def test2():
# 树中结点含有分叉，树B是树A的子结构
#                  8                8
#              /       \           / \
#             8         7         9   2
#           /   \
#          9     3
#               / \
#              4   7
    tree = BinaryTree()
    tree.root = Node(8)
    second1 = tree.root.left = Node(8)
    second2 = tree.root.right = Node(7)
    third1 = second1.left = Node(9)
    third2 = second1.right = Node(3)
    third2.left = Node(4)
    third2.right = Node(7)

    sub_tree = BinaryTree()
    sub_tree.root = Node(8)
    sub_tree.root.left = Node(9)
    sub_tree.root.right = Node(2)
    result = SubTree(tree.root,sub_tree.root)
    Test("Test2",result,False)

def test3():
# 树中结点含有分叉，树B是树A的子结构
#                8               8
#              /                /
#             8                9
#           /                 /
#          9                 2
#         /
#        2
#       /
#      5
    tree = BinaryTree()
    tree.root = Node(8)
    second = tree.root.left = Node(8)
    third = second.left = Node(9)
    forth = third.left = Node(2)
    fifth = forth.left = Node(5)


    sub_tree = BinaryTree()
    sub_tree.root = Node(8)
    sub_tree.root.left = Node(9)
    sub_tree.root.left.left = Node(2)
    result = SubTree(tree.root,sub_tree.root)
    Test("Test3",result,True)

def test4():
# 树中结点含有分叉，树B是树A的子结构
#                8               8
#              /                /
#             8                9
#           /                 /
#          9                 2
#         /
#        3
#       /
#      5
    tree = BinaryTree()
    tree.root = Node(8)
    second = tree.root.left = Node(8)
    third = second.left = Node(9)
    forth = third.left = Node(3)
    fifth = forth.left = Node(5)


    sub_tree = BinaryTree()
    sub_tree.root = Node(8)
    sub_tree.root.left = Node(9)
    sub_tree.root.left.left = Node(2)
    result = SubTree(tree.root,sub_tree.root)
    Test("Test4",result,False)

def test5():
# 树中结点含有分叉，树B是树A的子结构
#           8               8
#            \               \
#             8               9
#              \               \
#               9               2
#                \
#                 2
#                  \
#                   5
    tree = BinaryTree()
    tree.root = Node(8)
    second = tree.root.right = Node(8)
    third = second.right = Node(9)
    forth = third.right = Node(2)
    fifth = forth.right = Node(5)


    sub_tree = BinaryTree()
    sub_tree.root = Node(8)
    sub_tree.root.right = Node(9)
    sub_tree.root.right.right = Node(2)
    result = SubTree(tree.root,sub_tree.root)
    Test("Test5",result,True)

def test6():
# 树中结点含有分叉，树B是树A的子结构
#           8               8
#            \               \
#             8               9
#              \               \
#               9               2
#                \
#                 3
#                  \
#                   5
    tree = BinaryTree()
    tree.root = Node(8)
    second = tree.root.right = Node(8)
    third = second.right = Node(9)
    forth = third.right = Node(3)
    fifth = forth.right = Node(5)


    sub_tree = BinaryTree()
    sub_tree.root = Node(8)
    sub_tree.root.right = Node(9)
    sub_tree.root.right.right = Node(2)
    result = SubTree(tree.root,sub_tree.root)
    Test("Test6",result,False)

def test7():
    #A为空树
    tree = BinaryTree()

    sub_tree = BinaryTree()
    sub_tree.root = Node(8)
    sub_tree.root.right = Node(9)
    sub_tree.root.right.right = Node(2)
    result = SubTree(tree.root,sub_tree.root)
    Test("Test7",result,False)


def test8():
    # B为空树
    tree = BinaryTree()
    tree.root = Node(8)
    second = tree.root.left = Node(8)
    third = second.left = Node(9)
    forth = third.left = Node(3)
    fifth = forth.left = Node(5)

    sub_tree = BinaryTree()
    result = SubTree(tree.root, sub_tree.root)
    Test("Test8", result, False)


def test9():
    # AB均为空树
    tree = BinaryTree()
    sub_tree = BinaryTree()
    result = SubTree(tree.root, sub_tree.root)
    Test("Test9", result, False)

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


