# coding = utf-8
# author: Biyoner

def Sum_Solution1(n):
    return (n>0) and (n + Sum_Solution1(n-1))

def Sum_Solution2(n):
    return  sum(list(range(1, 1 + n)))


def Test(name, n, expect):
    if Sum_Solution1(n) == expect:
        print name +" is passed !"
    else:
        print name + " is failed !"

if __name__ == "__main__":
    Test("Test1",1,1)
    Test("Test2", 5, 15)
    Test("Test3", 10, 55)
    Test("Test4", 0, 0)