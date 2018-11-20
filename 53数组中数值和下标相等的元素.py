# coding= utf-8
# author:Biyoner

def GetNumberSameAsIndex(numbers):
    if len(numbers)<= 0:
        return -1
    start = 0
    end = len(numbers)-1
    while start<= end:
        center = (start + end) // 2
        if numbers[center] < center:
            start = center + 1
        elif numbers[center] > center:
            end = center - 1
        else:
            return center

    return -1

def Test(name,numbers,expectedValue):
    if GetNumberSameAsIndex(numbers) == expectedValue:
        print name + " is passed !"
    else:
        print name + " is failed !"

if __name__ =="__main__":
    Test("Test1", [-3, -1, 1, 3, 5],3)
    Test("Test2", [0, 1, 3, 5, 6 ], 0)
    Test("Test3", [-1, 0, 1, 2, 4], 4)
    Test("Test4", [-1, 0, 1, 2, 5 ], -1)
    Test("Test5", [0], 0)
    Test("Test6", [ 10], -1)
    Test("Test7", [], -1)

