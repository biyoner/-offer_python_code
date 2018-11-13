# coding=utf-8
# author:Biyoner
class Node(object):
    def __init__(self,data):
        self.data = data
        self.pnext = None

class circleLT(object):
    def __init__(self):
        self.head = None
    def create(self,dataOrNode,circlePoint=None):
        if not isinstance(dataOrNode,Node):
            node = Node(dataOrNode)
        else:
            node = dataOrNode

        if not self.head:
            self.head = node
        return node

    def createLink(self, node1, node2):
        if node1 and node2:
            node1.pnext = node2

def isCircle(ctl):
    circleL = 0
    flag = False
    count = 0
    p1 = ctl.head
    p2 = ctl.head
    if not ctl.head:
        return flag, circleL
    while p1.pnext:
        count+=1
        if count&1:
            p1 = p1.pnext
        else:
            p1 = p1.pnext
            p2 = p2.pnext
        if p1 == p2:
            flag = True
            break
    if flag:
        p2 = p2.pnext
        circleL += 1
        while p1!=p2:
            p2 = p2.pnext
            circleL += 1
    return flag,circleL

def findEntrance(ctl,n):
    p1 = ctl.head
    p2 = ctl.head
    for i in range(n):
        p1 = p1.pnext
    while p1 != p2:
        p1 = p1.pnext
        p2 = p2.pnext

    return p1

def Test(name, ctl, result):
    flag, circleL = isCircle(ctl)
    if flag and circleL > 0:
        entrance_p = findEntrance(ctl, circleL)
        test = entrance_p.data
    else:
        test = None
    if test == result:
        print name + " " + "is passed !"
    else:
        print name + " " + "is failed !"

def test1():
    name = "Test1"
    ctl = circleLT()
    ctl.create(1)
    Test(name,ctl,None)

def test2():
    name = "Test2"
    ctl = circleLT()
    pnode1 = ctl.create(1)
    ctl.createLink(pnode1,pnode1)
    Test(name, ctl, 1)

def test3():
    name = "Test3"
    ctl = circleLT()
    pnode1 = ctl.create(1)
    pnode2 = ctl.create(2)
    pnode3 = ctl.create(3)
    pnode4 = ctl.create(4)
    pnode5 = ctl.create(5)
    ctl.createLink(pnode1,pnode2)
    ctl.createLink(pnode2, pnode3)
    ctl.createLink(pnode3, pnode4)
    ctl.createLink(pnode4, pnode5)
    ctl.createLink(pnode5, pnode3)
    Test(name, ctl, 3)

def test4():
    name = "Test4"
    ctl = circleLT()
    pnode1 = ctl.create(1)
    pnode2 = ctl.create(2)
    pnode3 = ctl.create(3)
    pnode4 = ctl.create(4)
    pnode5 = ctl.create(5)
    ctl.createLink(pnode1, pnode2)
    ctl.createLink(pnode2, pnode3)
    ctl.createLink(pnode3, pnode4)
    ctl.createLink(pnode4, pnode5)
    ctl.createLink(pnode5, pnode1)
    Test(name, ctl, 1)
def test5():
    name = "Test5"
    ctl = circleLT()
    pnode1 = ctl.create(1)
    pnode2 = ctl.create(2)
    pnode3 = ctl.create(3)
    pnode4 = ctl.create(4)
    pnode5 = ctl.create(5)
    ctl.createLink(pnode1, pnode2)
    ctl.createLink(pnode2, pnode3)
    ctl.createLink(pnode3, pnode4)
    ctl.createLink(pnode4, pnode5)
    ctl.createLink(pnode5, pnode5)
    Test(name, ctl, 5)
def test6():
    name = "Test6"
    ctl = circleLT()
    pnode1 = ctl.create(1)
    pnode2 = ctl.create(2)
    pnode3 = ctl.create(3)
    pnode4 = ctl.create(4)
    pnode5 = ctl.create(5)
    ctl.createLink(pnode1, pnode2)
    ctl.createLink(pnode2, pnode3)
    ctl.createLink(pnode3, pnode4)
    ctl.createLink(pnode4, pnode5)
    Test(name, ctl, None)
def test7():
    name = "Test7"
    ctl = circleLT()
    # ctl.create(1)
    Test(name, ctl, None)

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()








    # Test("Test7", [], None, None)



