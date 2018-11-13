#coding= utf-8
#author:Biyoner

class Node(object):
    def __init__(self,data):
        self.data = data
        self.pnext = None
        self.pSibling = None

class LinkTable(object):
    def __init__(self):
        self.head = None

def BuildNodes(pnode1,pnode2,pnode3=None):
    pnode1.pnext = pnode2
    pnode1.pSibling = pnode3

def printTable(lt):
    if not lt:
        return None
    p = lt.head
    datas = []
    while p:
        if p.pSibling:
            datas.append(str(p.data)+"-"+str(p.pSibling.data))
        else:
            datas.append(str(p.data))
        p =p.pnext
    return datas


def CloneNodes(lt):
    if not lt.head:
        return None
    #First step
    p = lt.head
    while p:
        new = Node(p.data)
        new.pnext = p.pnext
        p.pnext = new
        p = p.pnext.pnext
    #Second Step
    p = lt.head
    while p:
        if p.pSibling:
            p.pnext.pSibling = p.pSibling.pnext
        else:
            p.pnext.pSibling = None
        p = p.pnext.pnext
    #Third Step
    p = lt.head
    lt_cloned = LinkTable()
    p_cloned = lt_cloned.head =p.pnext
    while p_cloned.pnext:
        p.pnext = p_cloned.pnext
        p = p.pnext
        p_cloned.pnext = p.pnext
        p_cloned = p_cloned.pnext
    p.pnext = None
    return lt_cloned

#          -----------------
#         \|/              |
#  1-------2-------3-------4-------5
#  |       |      /|\             /|\
#  --------+--------               |
#          -------------------------
def test1():
    lt = LinkTable()
    pNode1 = Node(1)
    pNode2 = Node(2)
    pNode3 = Node(3)
    pNode4 = Node(4)
    pNode5 = Node(5)
    lt.head = pNode1
    BuildNodes(pNode1, pNode2, pNode3)
    BuildNodes(pNode2, pNode3, pNode5)
    BuildNodes(pNode3, pNode4, None)
    BuildNodes(pNode4, pNode5, pNode2)
    # printTable(lt)
    newlt = CloneNodes(lt)
    print printTable(newlt)

# m_pSibling指向结点自身
#          -----------------
#         \|/              |
#  1-------2-------3-------4-------5
#         |       | /|\           /|\
#         |       | --             |
#         |------------------------|
def test2():
    lt = LinkTable()
    pNode1 = Node(1)
    pNode2 = Node(2)
    pNode3 = Node(3)
    pNode4 = Node(4)
    pNode5 = Node(5)
    lt.head = pNode1
    BuildNodes(pNode1, pNode2, None)
    BuildNodes(pNode2, pNode3, pNode5)
    BuildNodes(pNode3, pNode4, pNode3)
    BuildNodes(pNode4, pNode5, pNode2)
    # printTable(lt)
    newlt = CloneNodes(lt)
    print printTable(newlt)

# m_pSibling形成环
#          -----------------
#         \|/              |
#  1-------2-------3-------4-------5
#          |              /|\
#          |               |
#          |---------------|
def test3():
    lt = LinkTable()
    pNode1 = Node(1)
    pNode2 = Node(2)
    pNode3 = Node(3)
    pNode4 = Node(4)
    pNode5 = Node(5)
    lt.head = pNode1
    BuildNodes(pNode1, pNode2, None)
    BuildNodes(pNode2, pNode3, pNode4)
    BuildNodes(pNode3, pNode4, None)
    BuildNodes(pNode4, pNode5, pNode2)
    # printTable(lt)
    newlt = CloneNodes(lt)
    print printTable(newlt)

# 只有一个结点
def test4():
    lt = LinkTable()
    pNode1 = Node(1)
    lt.head = pNode1
    BuildNodes(pNode1, None, pNode1)
    # printTable(lt)
    newlt = CloneNodes(lt)
    print printTable(newlt)

# 鲁棒性测试
def test5():
    lt = LinkTable()
    newlt = CloneNodes(lt)
    print printTable(newlt)
    
if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()



