# coding=utf-8
# author:Biyoner
class Node(object):
    def __init__(self, data, left= None, right=None, parent =None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

def FindNext(node):
    if node == None:
        return "Error"
    if node.right:
        cur = node.right
        while cur.left:
            cur = cur.left
    else:
        if node == node.parent.left:
            cur = node.parent
        else:
            cur = None
            while node.parent:
                # print node.data
                if node.parent.left == node:
                    cur = node.parent
                node = node.parent

    return cur

if __name__ == "__main__":

    n3 = Node("d")
    n7 = Node("h")
    n8 = Node("i")
    n5 = Node("f")
    n6 = Node("g")
    n4 = Node("e",n7,n8)
    n1 = Node("b",n3,n4)
    n2= Node("c",n5,n6)
    root = Node("a",n1,n2)

    n1.parent = root
    n2.parent = root
    n3.parent = n1
    n4.parent = n1
    n5.parent = n2
    n6.parent = n2
    n7.parent = n4
    n8.parent = n4

    print root.parent

    test = [root,n1,n2,n3,n4,n5,n6,n7,n8]
    result =[]
    for item in test:
        cur = FindNext(item)
        if cur:
            print cur.data
            result.append(cur.data)
        else:
            result.append(cur)
    print result
