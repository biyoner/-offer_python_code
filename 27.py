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
    def preOrderPrint(self,root):
        datas = []
        if root:
            datas.append(root.data)
            return datas + self.preOrderPrint(root.left) + self.preOrderPrint(root.right)
        else:
            return datas

def MirrorRecursive(root):
    if root:
        temp = root.left
        root.left = root.right
        root.right = temp
        MirrorRecursive(root.left)
        MirrorRecursive(root.right)

# ====================测试代码====================
# 测试完全二叉树：除了叶子节点，其他节点都有两个子节点
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
    print tree.preOrderPrint(tree.root)

    MirrorRecursive(tree.root)
    print tree.preOrderPrint(tree.root)

#测试二叉树：出叶子结点之外，左右的结点都有且只有一个左子结点
#            8
#          7
#        6
#      5
#    4
def test2():
    tree = BinaryTree()
    tree.root = Node(8)
    tree.root.left = Node(7)
    tree.root.left.left = Node(6)
    tree.root.left.left.left= Node(5)
    tree.root.left.left.left.left = Node(4)
    print tree.preOrderPrint(tree.root)

    MirrorRecursive(tree.root)
    print tree.preOrderPrint(tree.root)


#测试二叉树：出叶子结点之外，左右的结点都有且只有一个右子结点
#           8
#             7
#              6
#               5
#                4
def test3():
    tree = BinaryTree()
    tree.root = Node(8)
    tree.root.right = Node(7)
    tree.root.right.right = Node(6)
    tree.root.right.right.right= Node(5)
    tree.root.right.right.right.right = Node(4)
    print tree.preOrderPrint(tree.root)

    MirrorRecursive(tree.root)
    print tree.preOrderPrint(tree.root)

# 测试空二叉树：根结点为空指针
def test4():
    tree = BinaryTree()
    print tree.preOrderPrint(tree.root)

    MirrorRecursive(tree.root)
    print tree.preOrderPrint(tree.root)

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
