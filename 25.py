#coding= utf-8
#author: biyoner
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

def Merge(lt1, lt2):
    p1 = lt1.head
    p2 = lt2.head
    if lt1.head==None:
        return lt2
    if lt2.head==None:
        return lt1

    merge = LinkTable()
    if p1.data < p2.data:
        lt1.head = p1.pnext
        merge.head = Node(p1.data)
    else:
        lt2.head = p2.pnext
        merge.head = Node(p2.data)
    pm = merge.head
    pm = MergeCore(lt1,lt2,pm)
    return merge



def MergeCore(lt1,lt2,pm):
    if lt1.head==None:
        pm.pnext = lt2.head
        return pm
    if lt2.head==None:
        pm.pnext = lt1.head
        return pm
    p1 = lt1.head
    p2 = lt2.head
    if p1.data < p2.data:
        pm.pnext = Node(p1.data)
        pm = pm.pnext
        lt1.head = p1.pnext
        MergeCore(lt1,lt2,pm)
    else:
        pm.pnext = Node(p2.data)
        pm = pm.pnext
        lt2.head = p2.pnext
        MergeCore(lt1, lt2, pm)
    return pm


def test1():
    lt1 = LinkTable()
    lt1.create(1)
    lt1.create(3)
    lt1.create(5)

    lt2 = LinkTable()
    lt2.create(2)
    lt2.create(4)
    lt2.create(6)
    merge = Merge(lt1, lt2)
    print merge.printLT()
def test2():
    lt1 = LinkTable()
    lt1.create(1)
    lt1.create(3)
    lt1.create(5)
    lt2 = LinkTable()
    lt2.create(1)
    lt2.create(3)
    lt2.create(5)
    merge = Merge(lt1, lt2)
    print merge.printLT()
def test3():
    lt1 = LinkTable()
    lt1.create(1)
    lt2 = LinkTable()
    lt2.create(2)
    merge = Merge(lt1, lt2)
    print merge.printLT()

def test4():
    lt1 = LinkTable()
    lt1.create(1)
    lt1.create(3)
    lt1.create(5)
    lt2 = LinkTable()
    merge = Merge(lt1, lt2)
    print merge.printLT()
def test5():
    lt1 = LinkTable()
    lt2 = LinkTable()
    merge = Merge(lt1, lt2)
    print merge.printLT()
if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()


