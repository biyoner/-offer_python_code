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

def reverseLink(lt):
    p_pre = p = p_next = lt.head
    if not p:
        return None
    if p.pnext:
        p = p_next = p.pnext
    else:
        return lt
    if p_pre == lt.head:
        p_pre.pnext = None
    while p_next.pnext:
        p_next = p_next.pnext
        p.pnext = p_pre
        p_pre = p
        p = p_next
    p.pnext = p_pre
    lt.head = p_next
def Test(name, lt, result):

    reverseLink(lt)
    # print lt.printLT()
    if lt.printLT() == result:
        print name+" " + "is passed !"
    else:
        print name+" " + "is failed !"

def test1():
    data  = [1,2,3,4,5]
    lt = LinkTable()
    for i in data:
        lt.create(i)
    data.reverse()
    Test("test1",lt,data)
def test2():
    data  = [1]
    lt = LinkTable()
    for i in data:
        lt.create(i)
    data.reverse()
    Test("test2",lt,data)
def test3():
    data = []
    lt = LinkTable()
    for i in data:
        lt.create(i)
    data.reverse()
    Test("test3", lt,data)

if __name__ == "__main__":
    test1()
    test2()
    test3()