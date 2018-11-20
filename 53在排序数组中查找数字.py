# coding= utf-8
# author:Biyoner

def GetFirstK(data,k,start,end):
    if start > end:
        return -1

    middleIndex = (start + end) /2
    if data[middleIndex] == k:
        if middleIndex > 0 and data[middleIndex-1] == k:
            end = middleIndex -1
        else:
            return middleIndex
    elif data[middleIndex] <k:
        start = middleIndex + 1
    else:
        end = middleIndex - 1

    return GetFirstK(data,k,start,end)

def GetEndK(data, k, start, end):
    if start > end:
        return -1

    middleIndex = (start + end) /2
    if data[middleIndex] == k:
        if middleIndex<end and data[middleIndex+1] == k:
            start = middleIndex + 1
        else:
            return middleIndex
    elif data[middleIndex] <k:
        start = middleIndex + 1
    else:
        end = middleIndex - 1

    return  GetEndK(data,k,start,end)

def GetNumberOfK(data,k):
    if len(data)<=0:
        return 0
    number = 0

    first = GetFirstK(data,k,0,len(data)-1)
    end = GetEndK(data,k,0,len(data)-1)

    if first>-1 and end >-1:
        number = end - first + 1
    return number

# 查找的数字出现在数组的中间
def Test1():
    data = [1, 2, 3, 3, 3, 3, 4, 5]
    Test("Test1", data, 3, 4)


# 查找的数组出现在数组的开头
def Test2():
    data = [3, 3, 3, 3, 4, 5]
    Test("Test2", data,  3, 4)


# 查找的数组出现在数组的结尾
def Test3():
    data = [1, 2, 3, 3, 3, 3]
    Test("Test3", data,  3, 4)


# 查找的数字不存在
def Test4():
    data= [1, 3, 3, 3, 3, 4, 5]
    Test("Test4", data, 2, 0)

# 查找的数字比第一个数字还小，不存在
def Test5():

    data = [1, 3, 3, 3, 3, 4, 5]
    Test("Test5",data, 0, 0)


# 查找的数字比最后一个数字还大，不存在
def Test6():

    data = [1, 3, 3, 3, 3, 4, 5]
    Test("Test6", data, 6, 0)


# 数组中的数字从头到尾都是查找的数字
def Test7():

    data = [3, 3, 3, 3]
    Test("Test7", data,  3, 4)

# 数组中的数字从头到尾只有一个重复的数字，不是查找的数字
def Test8():
    data = [3, 3, 3, 3]
    Test("Test8", data, 4, 0)


# 数组中只有一个数字，是查找的数字
def Test9():
    data = [3]
    Test("Test9", data,  3, 1)


# 数组中只有一个数字，不是查找的数字
def Test10():
    data = [3]
    Test("Test10", data,  4, 0)


# 鲁棒性测试，数组空指针
def Test11():

    Test("Test11", [], 0, 0)


def Test(name,data,k,expectedValue):
    if GetNumberOfK(data,k) == expectedValue:
        print name + " is passed !"
    else:
        print name + " is failed !"

if __name__ == "__main__":
    Test1()
    Test2()
    Test3()
    Test4()
    Test5()
    Test6()
    Test7()
    Test8()
    Test9()
    Test10()
    Test11()