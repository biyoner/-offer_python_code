#coding= utf-8
#author:Biyoner


def IsUgly(n):
    while n%2 == 0:
        n /=2
    while n%3 == 0:
        n /= 3
    while n%5 == 0:
        n /= 5
    if n == 1:
        return True
    else:
        return False

def GetUglyNumber1(index):
    if index <= 0:
        return 0
    number = 0
    uglyFound = 0
    while uglyFound<index:
        number += 1
        if IsUgly(number):
            # print number
            uglyFound += 1
    return number


def GetUglyNumber2(index):
    if index <= 0:
        return 0
    numbers = [1]
    M2 = 0
    M3 = 0
    M5 = 0
    for _ in range(index-1):
        minNum = min(numbers[M2]*2,numbers[M3]*3,numbers[M5]*5)
        numbers.append(minNum)
        if minNum == numbers[M2]*2:
            M2 += 1
        if minNum == numbers[M3]*3:
            M3 += 1
        if minNum == numbers[M5]*5:
            M5 += 1
    return numbers[-1]


def Test(name, index, expectedValue):
    if GetUglyNumber2(index) == expectedValue:
        print name + " is passed !"
    else:
        print name + " is failed !"

if __name__ == "__main__":
    Test("Test1",1, 1)
    Test("Test2",2, 2)
    Test("Test3",3, 3)
    Test("Test4",4, 4)
    Test("Test5",5, 5)
    Test("Test6",6, 6)
    Test("Test7",7, 8)
    Test("Test8",8, 9)
    Test("Test9",9, 10)
    Test("Test10",10, 12)
    Test("Test11",11, 15)
    Test("Test12",1500, 859963392)
    Test("Test13",0, 0)
    #

    # print GetUglyNumber(1500)
    # print  IsUgly(36)