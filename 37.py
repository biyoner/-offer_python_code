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

def Serialize(root):
    if not root:
        return ["$"]
    left = Serialize(root.left)
    right = Serialize(root.right)
    return [str(root.data)] + left + right


def Deserialize(l):
    if l[0] == "$":
        root = None
        return root,l[1:]
    root = Node(l[0])
    root.left,l= Deserialize(l[1:])
    root.right,l = Deserialize(l)
    return root,l

def preorder(root):
    if root is None:
        return []
    result = [root.data]
    left_tree = preorder(root.left)
    right_tree = preorder(root.right)
    return result + left_tree +right_tree

#            8
#        6      10
#       5 7    9  11
def test1():
    tree = BinaryTree()
    tree.root = Node(8)
    tree.root.left = Node(6)
    tree.root.right = Node(10)
    tree.root.left.left = Node(5)
    tree.root.left.right = Node(7)
    tree.root.right.left = Node(9)
    tree.root.right.right = Node(11)
    l = Serialize(tree.root)
    print "Test1"
    print "Serialize list: ",l
    tree, _ = Deserialize(l)
    print "Deserialize list: ",preorder(tree)
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
    l = Serialize(tree.root)
    print "Test2"
    print "Serialize list: ",l
    tree, _ = Deserialize(l)
    print "Deserialize list: ",preorder(tree)

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
    l = Serialize(tree.root)
    print "Test3"
    print "Serialize list: ",l
    tree, _ = Deserialize(l)
    print "Deserialize list: ",preorder(tree)


def test4():
    tree = BinaryTree()
    tree.root = Node(5)
    l = Serialize(tree.root)
    print "Test4"
    print "Serialize list: ", l
    tree, _ = Deserialize(l)
    print "Deserialize list: ", preorder(tree)

def test5():
    tree = BinaryTree()
    l = Serialize(tree.root)
    print "Test5"
    print "Serialize list: ", l
    tree, _ = Deserialize(l)
    print "Deserialize list: ", preorder(tree)

#        5
#         5
#          5
#         5
#        5
#       5 5
#      5   5
def test6():
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.right = Node(5)
    tree.root.right.right = Node(5)
    tree.root.right.right.left = Node(5)
    tree.root.right.right.left.left = Node(5)
    tree.root.right.right.left.left.left = Node(5)
    tree.root.right.right.left.left.left.left = Node(5)
    tree.root.right.right.left.left.right = Node(5)
    tree.root.right.right.left.left.right.right = Node(5)
    l = Serialize(tree.root)
    print "Test6"
    print "Serialize list: ", l
    tree, _ = Deserialize(l)
    print "Deserialize list: ", preorder(tree)
if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()


