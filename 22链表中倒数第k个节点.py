# coding=utf-8
# author:Biyoner
class Node(object):
    def __init__(self,data):
        self.data = data
        self.pnext = None

class LinkTable(object):
    def __init__(self):
        self.head = None
    def create(self, dataOrNode):
        if not isinstance(dataOrNode,Node):
            node = Node(dataOrNode)
        else:
            node = dataOrNode

        if not self.head:
            self.head = node
        else:
            p = self.head
            while p.pnext:
                p = p.pnext
            p.pnext = node
    def printLT(self):
        datas = []
        p = self.head
        while p:
            datas.append(p.data)
            p = p.pnext
        return datas

def printLastK(lt,k):
    if k<=0:
        return None
    p1 = lt.head
    p2 = lt.head
    for _ in range(k-1):
        if not p1 or (not p1.pnext):
            return None
        else:
            p1 = p1.pnext
    while p1.pnext:
        p1 = p1.pnext
        p2 = p2.pnext
    return p2.data
def Test(name,l,k,result):
    lt = LinkTable()
    vals = l
    for i in vals:
        lt.create(i)
    # print lt.printLT()
    if printLastK(lt, k) == result:
        print name +" "+ "is passed !"
    else:
        print name + " " + "is failed !"

if __name__ == "__main__":
    lt = LinkTable()
    Test("Test1",[1,2,3,4,5],2,4)
    Test("Test2", [1, 2, 3, 4, 5], 1, 5)
    Test("Test3", [1, 2, 3, 4, 5], 5, 1)
    Test("Test4", [], 100, None)
    Test("Test5", [1, 2, 3, 4, 5], 6, None)
    Test("Test6", [1, 2, 3, 4, 5], 0, None)


