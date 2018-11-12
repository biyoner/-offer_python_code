#coding= utf-8
#author:Biyoner

def MoreThanHalfNum(l):
    k = len(l) // 2
    val = Partition(0,len(l)-1,l,k)
    return val

def MoreThanHalfNum2(l):
    val = 0
    times = 0
    for i in l:
        if i == val:
            times += 1
        else:
            if times>0:
                times-=1
            else:
                val = i
    return val




def Partition(begin,end,l,index):
    i = begin
    j = end
    base = l[begin]
    while i<j:
        while (l[j] >= base) and i< j:
            j -= 1
        l = swap(i,j,l)
        while l[i]<= base and i< j:
            i += 1
        l = swap(i,j,l)
    if i < index:
        return Partition(i+1,end,l,index)
    elif i > index:
        return Partition(begin,i-1,l,index)
    else:
        return l[index]

def swap(i,j,l):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp
    return l

def checklist(l):
    flag = False
    if len(l) <= 0:
        flag = True
    return flag

def Test(name, numbers, expectValue,expectflag):
    if checklist(numbers) == False:
        result = MoreThanHalfNum(numbers)
        # result = MoreThanHalfNum2(numbers)
        MoreThanHalf_Flag = checkMoreThanHalf(numbers,result)
        if MoreThanHalf_Flag:
            result = 0
        if  result == expectValue:
            print name+ " is passed!"
        else:
            print name+ " is failed!"
    else:
        if checklist(numbers) == expectflag:
            print name + " is passed!"
        else:
            print name+ " is failed!"

def checkMoreThanHalf(l,result):
    times = 0
    for item in l:
        if item == result:
            times+=1
    if times*2 <len(l):
        return True
    else:
        return False

if __name__ == "__main__":
    Test("Test1",[1, 2, 3, 2, 2, 2, 5, 4, 2],2,False)
    Test("Test2", [1, 2, 3, 2, 4, 2, 5, 2, 3], 0, True)
    Test("Test3", [2, 2, 2, 2, 2, 1, 3, 4, 5], 2, False)
    Test("Test4", [1, 3, 4, 5, 2, 2, 2, 2, 2], 2, False)
    Test("Test5", [1], 1, False)
    Test("Test6", [], 0, True)
