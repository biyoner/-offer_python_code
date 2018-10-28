# coding=utf-8
# author:Biyoner
class Node(object):
    def __init__(self,data):
        self.data = data
        self.pnext = None

class linkTable(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def add_Node(self,NodeorData):
        if not isinstance(NodeorData,Node):
            n = Node(NodeorData)
        else:
            n = NodeorData
        if not self.head:
            self.head = n
        else:
            p = self.head
            while p.pnext:
                p = p.pnext
            p.pnext = n
        self.length += 1

    def printLinkTable(self):
        datas = []
        if self.length == 0:
            return "The linktable is None"
        p = self.head
        while p:
            datas.append(p.data)
            p = p.pnext
        return datas

    def deleteNoede(self,p_delete):
        if self.length == 0 or not Node:
            return
        if p_delete.pnext:
            p_delete.data = p_delete.pnext.data
            p_delete.pnext = p_delete.pnext.pnext
        elif self.length == 1:
            self.head = None
        else:
            p = self.head
            while p.pnext != p_delete:
                p = p.pnext
            p.pnext = None

    def deleteDuplication(self):
        p = self.head
        p_pre = None
        flag = False

        if not p:
            return "The linktable is Null"

        while p and p.pnext:
            if p.data == p.pnext.data:
                flag = True
            else:
                p_pre = p
                p = p.pnext
            if flag == True:
                while p.pnext:
                    if p.pnext.data>p.data:
                        break
                    else:
                        p = p.pnext
                p = p.pnext
                if p_pre == None:
                    self.head = p
                else:
                    p_pre.pnext = p
                flag = False


if __name__ == "__main__":
    ### Test delete single Node in O(1)
    lt = linkTable()
    for i in range(20):
        lt.add_Node(i)
    print lt.printLinkTable()
    p = lt.head
    for _ in range(5):
        p = p.pnext
    lt.deleteNoede(p)
    print lt.printLinkTable()
    ### Test delete all duplicated nodes where the linktable is in order
    lt = linkTable()
    #1
    lt.add_Node(1)
    lt.add_Node(2)
    lt.add_Node(3)
    lt.add_Node(3)
    lt.add_Node(4)
    lt.add_Node(4)
    lt.add_Node(5)
    #2
    lt.add_Node(1)
    lt.add_Node(2)
    lt.add_Node(3)
    lt.add_Node(4)
    lt.add_Node(5)
    lt.add_Node(6)
    lt.add_Node(7)
    # #3
    lt.add_Node(1)
    lt.add_Node(1)
    lt.add_Node(1)
    lt.add_Node(1)
    lt.add_Node(1)
    lt.add_Node(1)
    lt.add_Node(2)
    # #4
    lt.add_Node(1)
    lt.add_Node(1)
    lt.add_Node(1)
    lt.add_Node(1)
    lt.add_Node(1)
    lt.add_Node(1)
    lt.add_Node(1)
    # #5
    lt.add_Node(1)
    lt.add_Node(1)
    lt.add_Node(2)
    lt.add_Node(2)
    lt.add_Node(3)
    lt.add_Node(3)
    lt.add_Node(4)
    lt.add_Node(4)
    # #6
    lt.add_Node(1)
    lt.add_Node(1)
    lt.add_Node(2)
    lt.add_Node(3)
    lt.add_Node(3)
    lt.add_Node(4)
    lt.add_Node(5)
    lt.add_Node(5)
    # #7
    lt.add_Node(1)
    lt.add_Node(2)
    # #8
    lt.add_Node(1)
    # #9
    lt.add_Node(1)
    lt.add_Node(1)

    print lt.printLinkTable()
    lt.deleteDuplication()
    print lt.printLinkTable()


