# coding= utf-8
# author:Biyoner

def GetMissingNumber(numbers):
    if len(numbers)<=0:
        return -1

    start = 0
    end = len(numbers)-1

    while start<=end:
        center = (start + end) /2
        if numbers[center] == center:
            start = center + 1
        else:
            if center==0 or numbers[center-1]==center-1:
                return center
            end = center - 1
    
    if start == len(numbers):
        return len(numbers)

    return  -1

def Test(name,numbers,expectedValue):
    if GetMissingNumber(numbers) == expectedValue:
        print name + " is passed !"
    else:
        print name + " is failed !"

# 缺失的是第一个数字0
def Test1():
    numbers = [1, 2, 3, 4, 5]
    expected = 0
    Test("Test1", numbers, expected)

# 缺失的是最后一个数字
def Test2():
    numbers = [0, 1, 2, 3, 4]
    expected = 5
    Test("Test2", numbers, expected)

# 缺失的是中间某个数字0
def Test3():
    numbers = [0, 1, 2, 4, 5]
    expected = 3
    Test("Test3", numbers, expected)


# 数组中只有一个数字，缺失的是第一个数字0
def Test4():
    numbers = [1]
    expected = 0
    Test("Test4", numbers, expected)

# 数组中只有一个数字，缺失的是最后一个数字1
def Test5():
    numbers = [0]
    expected = 1
    Test("Test5", numbers, expected)

# 空数组
def Test6():
    expected = -1
    Test("Test6", [], expected)

if __name__ == "__main__":
    Test1()
    Test2()
    Test3()
    Test4()
    Test5()
    Test6()



