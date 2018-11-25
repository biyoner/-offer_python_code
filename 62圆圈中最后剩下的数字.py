#coding = utf-8
#author: Biyoner

class Node(object):
    def __init__(self,data):
        self.data = data
        self.pnext = None


def LastRemaining_Solution1(n,m):
    if n <= 0:
        return -1

    p0 = Node(0)
    p = p0
    for i in range(1,n):
        p.pnext = Node(i)
        p = p.pnext
    p.pnext = p0

    p = p0
    while p.pnext!=p:
        for _ in range(m-2):
            p = p.pnext
        p.pnext = p.pnext.pnext
        p = p.pnext
    return p.data

def LastRemaining_Solution2(n,m):
    if n <= 0:
        return -1

    val = 0
    for i in range(2,n+1):
        val = (val+m) % i
    return val



def Test(name, n, m, expectValue):
    if LastRemaining_Solution2(n,m) == expectValue:
        print name + " is passed !"

    else:
        print name + " is failed !"

if __name__ == "__main__":
    Test("Test1", 5, 3, 3)
    Test("Test2", 5, 2, 2)
    Test("Test3", 6, 7, 4)
    Test("Test4", 6, 6, 3)
    Test("Test5", 0, 0, -1)
    Test("Test6", 4000, 997, 1027)

