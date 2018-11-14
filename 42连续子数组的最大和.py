#coding= utf-8
#author:Biyoner

def FindGreastSunOfSubArray(data):
    if len(data)<=0:
        return None

    ncurSum = 0
    nGreatestSum = float('-inf')

    for i in data:
        if ncurSum+i > i:
            ncurSum += i
        else:
            ncurSum = i

        if nGreatestSum < ncurSum:
            nGreatestSum = ncurSum

    return nGreatestSum

def Test(name,l,expectResult):
    if FindGreastSunOfSubArray(l) == expectResult:
        print name+" is passed !"
    else:
        print name+" is failed !"

if __name__ == "__main__":

    Test("Test1",[1,-2,3,10,-4,7,2,-5],18)

    Test("Test2", [-2, -8, -1, -5, -9], -1)

    Test("Test3", [2, 8, 1, 5, 9], 25)

    Test("Test4", [], None)
