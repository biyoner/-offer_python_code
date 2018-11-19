# coding= utf-8
# author:Biyoner
import copy
def InversePairs(data):
    if len(data) <= 0:
        return 0
    l = copy.copy(data)
    return InversePairCore(data,l,0,len(data)-1)

def InversePairCore(data,copy,start,end):
    if start == end:
        return 0

    center = (end + start) // 2
    left = InversePairCore(copy,data,start,center)
    right = InversePairCore(copy,data,center+1,end)

    i = center
    j = end
    indexCopy = end
    count = 0

    while i>=start and j>=center+1:
        if data[i] > data[j]:
            copy[indexCopy] = data[i]
            i -= 1
            indexCopy -= 1
            count += (j-center)
        else:
            copy[indexCopy] = data[j]
            j -= 1
            indexCopy -= 1

    while j>=center+1:
        copy[indexCopy]  = data[j]
        indexCopy -= 1
        j -= 1
    while i >= start:
        copy[indexCopy] = data[i]
        indexCopy -= 1
        i -= 1

    return left + right + count

def Test(name,data,expectedData):
    if InversePairs(data) == expectedData:
        print name + " is passed !"
    else:
        print name + " is failed !"

if __name__ == "__main__":
    Test("Test1",[1, 2, 3, 4, 7, 6, 5],3)
    Test("Test2", [6, 5, 4, 3, 2, 1], 15)
    Test("Test3", [1, 2, 3, 4, 5, 6 ], 0)
    Test("Test4", [1], 0)
    Test("Test5", [1, 2], 0)
    Test("Test6", [2, 1], 1)
    Test("Test7", [1, 2, 1, 2, 1], 3)
    Test("Test8", [], 0)