# coding=utf-8
# author:Biyoner

def find_repeat1(L):
    n = len(L)
    new = []
    value = None
    for i in range(n):
        if L[i] in new:
            #print L[i]
            value = L[i]
            break
        else:
            new.append(L[i])
    return value

def find_repeat2(L):
    n = len(L)
    repeat = False
    repeat_num = None

    if n<=0:
        return "The list is null"

    for i in range(n):
        if L[i] >n or L[i]<0:
            return "This list is not right"

    for i in range(n):
        val = L[i]
        while(val != i):
            if val == L[val]:
                repeat = True
                break
            else:
                L[i] = L[val]
                L[val] = val
                val = L[i]

        if repeat == True:
            repeat_num = L[i]
            break

    return repeat_num



if __name__ == "__main__":
    # testing lists
    l1 = [2,3,1,0,2,5,3]
    l2 = [0,2,1]
    l3 = []
    l4 = [2,3,10,3,8]
    l5 = [1,2,1]
    ls = [l1,l2,l3,l4,l5]
    for item in ls:
        print item
        val = find_repeat2(item)
        print val
