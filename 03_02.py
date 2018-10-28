# coding=utf-8
# author:Biyoner
def list_check(L):
    n = len(L)-1
    if n <0:
        return "The list is null"

    for i in range(len(L)):
        if L[i] >n or L[i]<1:
            return "The value is not valid"
    return True

def find_repeat1(L):
    n = len(L)
    new = []
    value = None
    for i in range(n):
        if L[i] in new:
            value = L[i]
            break
        else:
            new.append(L[i])
    return value

def count(L,start,end):
    n = len(L)
    cen = (start + end)/2
    left = []
    right = []
    if start!= end:
        for i in range(n):
            if L[i] <= cen:
                left.append(L[i])
            else:
                right.append(L[i])
            if len(left) >(cen-start+1):
                return count(left,start,cen)
            elif len(right) > (end-cen):
                return count(right,cen+1,end)
    else:
        return start




def find_repeat2(L):
    check = list_check(L)
    n = len(L)-1
    start = 1
    end = n
    if check == True:
        repeat = count(L,start,end)
        return repeat
    else:
        return check



if __name__ == "__main__":
    # testing lists
    l1 = [2, 3, 5, 4, 3, 2, 6, 7 ]
    l2 = [3, 2, 1, 4, 4, 5, 6, 7 ]
    l3 = [1, 2, 3, 4, 5, 6, 7, 1, 8]
    l4 = [1, 7, 3, 4, 5, 6, 8, 2, 8]
    l5 = [1, 1 ]
    l6 = [3, 2, 1, 3, 4, 5, 6, 7]
    l7 = [1, 2, 2, 6, 4, 5, 6]
    l8 = [1, 2, 2, 6, 4, 5, 2 ]
    l9 = [ 1, 2, 6, 4, 5, 3]
    l10= [-1]
    ls = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]

    for item in ls:
        print item
        val = find_repeat2(item)
        print val
