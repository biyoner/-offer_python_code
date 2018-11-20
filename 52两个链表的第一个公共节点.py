# coding= utf-8
# author:Biyoner

class ListNode(object):
    def __init__(self,data):
        self.m_nkey = data
        self.m_pNext = None

def ConnectListNodes(node1,node2):
    node1.m_pNext = node2


def FindFirstCommonNode(head1,head2):
    if not head1 or not head2:
        return None
    length1 = 0
    length2 = 0
    p = head1
    q = head2
    while p:
        length1 += 1
        p = p.m_pNext
    while q:
        length2 += 1
        q = q.m_pNext
    p = head1
    q = head2
    if length1>length2:
        while length1>length2:
            p = p.m_pNext
            length1 -= 1

    if length2 > length1:
        while length2 > length1:
            q = q.m_pNext
            length2 -= 1
    while p != q:
        p = p.m_pNext
        q = q.m_pNext
    return p
def Test(name, node1,node2,expectedValue):
    if FindFirstCommonNode(node1,node2) == expectedValue:
        print name + " is passed !"
    else:
        print name + " is failed !"

def test1():
    # 第一个公共结点在链表中间
    # 1 - 2 - 3 \
               # 6 - 7
    # 4 - 5 /
    pNode1 = ListNode(1)
    pNode2 = ListNode(2)
    pNode3 = ListNode(3)
    pNode4 = ListNode(4)
    pNode5 = ListNode(5)
    pNode6 = ListNode(6)
    pNode7 = ListNode(7)


    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode6)
    ConnectListNodes(pNode4, pNode5)
    ConnectListNodes(pNode5, pNode6)
    ConnectListNodes(pNode6, pNode7)

    Test("Test1", pNode1, pNode4, pNode6)

def test2():
    # 没有公共结点
    # 1 - 2 - 3 - 4
    #
    # 5 - 6 - 7
    pNode1 = ListNode(1)
    pNode2 = ListNode(2)
    pNode3 = ListNode(3)
    pNode4 = ListNode(4)
    pNode5 = ListNode(5)
    pNode6 = ListNode(6)
    pNode7 = ListNode(7)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode5, pNode6)
    ConnectListNodes(pNode6, pNode7)

    Test("Test2", pNode1, pNode5, None)

def test3():
    # 公共结点是最后一个结点
    # 1 - 2 - 3 - 4 \
                   # 7
    # 5 - 6 /
    pNode1 = ListNode(1)
    pNode2 = ListNode(2)
    pNode3 = ListNode(3)
    pNode4 = ListNode(4)
    pNode5 = ListNode(5)
    pNode6 = ListNode(6)
    pNode7 = ListNode(7)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode4, pNode7)
    ConnectListNodes(pNode5, pNode6)
    ConnectListNodes(pNode6, pNode7)

    Test("Test3", pNode1, pNode5, pNode7)

def test4():
    # 公共结点是第一个结点
    # 1 - 2 - 3 - 4 - 5
    # 两个链表完全重合
    pNode1 = ListNode(1)
    pNode2 = ListNode(2)
    pNode3 = ListNode(3)
    pNode4 = ListNode(4)
    pNode5 = ListNode(5)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode4, pNode5)
    Test("Test4", pNode1, pNode1, pNode1)

def test5():
    # 输入的两个链表有一个空链表
    pNode1 = ListNode(1)
    pNode2 = ListNode(2)
    pNode3 = ListNode(3)
    pNode4 = ListNode(4)
    pNode5 = ListNode(5)
    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode4, pNode5)

    Test("Test5", None, pNode1,  None)

def test6():
    Test("Test6", None, None, None)


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()




