#coding= utf-8
#author:Biyoner
def VerifySequenceOfBST(l):
    if len(l) <=0:
        return False

    root = l[-1]
    left = []
    right = []
    key = 0
    for i in range(len(l)-1):
        if l[i] < root:
            left.append(l[i])
            key = i + 1
        else:
            key = i
            break
    for j in range(key,len(l)-1):
        if l[j] > root:
            right.append(l[j])
        else:
            return False

    if len(left) == 0:
        return True
    if len(right) == 0:
        return True
    if VerifySequenceOfBST(left) and VerifySequenceOfBST(right):
        return True

def Test(name,l,result):
    if VerifySequenceOfBST(l) == result:
        print name + " " +"is passed !"
    else:
        print name + " " + "is failed !"

if __name__ == "__main__":

    Test("Test1",[4, 8, 6, 12, 16, 14, 10],True)
    Test("Test2", [4, 6, 7, 5], True)
    Test("Test3", [1, 2, 3, 4, 5], True)
    Test("Test4", [5, 4, 3, 2, 1], True)
    Test("Test5", [5], True)
    Test("Test6", [7, 4, 6, 5], False)
    Test("Test7", [4, 6, 12, 8, 16, 14, 10], False)
    Test("Test8", [], False)
