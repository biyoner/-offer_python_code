# coding=utf-8
# author:Biyoner
class Node(object):
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.l_tree = left
        self.r_tree = right


class Tree(object):
    def __init__(self,data):
        self.root = Node(data, left=None, right=None)

    def preorder(self,root):
        if root is None:
            return []
        result = [root.data]
        left_tree = self.preorder(root.l_tree)
        right_tree = self.preorder(root.r_tree)
        return result + left_tree +right_tree

    def inorder(self,root):
        if root is None:
            return []
        result = [root.data]
        left_tree = self.inorder(root.l_tree)
        right_tree = self.inorder(root.r_tree)
        return left_tree + result + right_tree

    def postorder(self,root):
        if root is None:
            return []
        result = [root.data]
        left_tree = self.postorder(root.l_tree)
        right_tree = self.postorder(root.r_tree)
        return left_tree + right_tree + result


def reconstruct(preorder,inorder):
    l1 = len(preorder)
    l2 = len(inorder)
    if l1 != l2:
        return "Error"
    if l1 == 0:
        return None
    root_val = preorder[0]
    root = Node(root_val)
    index = inorder.index(root_val)
    root.l_tree=reconstruct(preorder[1:index+1],inorder[0:index])
    root.r_tree = reconstruct(preorder[index+1:],inorder[index+1:])
    return root

def preorder(root):
    if root is None:
        return []
    result = [root.data]
    left_tree = preorder(root.l_tree)
    right_tree = preorder(root.r_tree)
    return result + left_tree +right_tree

if __name__ == '__main__':
    ##Construct a tree
    tree = Tree(1)
    tree.root.l_tree = Node(2, None, None)
    tree.root.r_tree = Node(3, None, None)
    tree.root.l_tree.l_tree = Node(4, None, None)
    tree.root.l_tree.r_tree = Node(5, None, None)
    tree.root.r_tree.l_tree = Node(6, None, None)
    tree.root.r_tree.r_tree = Node(7, None, None)
    tree.root.l_tree.l_tree.l_tree = Node(8, None, None)
    tree.root.l_tree.l_tree.r_tree = Node(9, None, None)
    tree.root.l_tree.r_tree.l_tree = Node(10, None, None)
    tree.root.l_tree.r_tree.l_tree = Node(11, None, None)
    print tree.preorder(tree.root)
    print tree.inorder(tree.root)
    print tree.postorder(tree.root)

    tree = reconstruct([1, 2, 4, 7,3,5,6,8],[4,7,2,1,5,3,8,6])
    print preorder(tree)





