#coding=utf-8
#author:Biyoner

def digitAtIndex(index):
    if index<=0:
        return 0
    digits = 1
    while 1:
        numbers = countOfIntegers(digits)
        if index > numbers*digits:
            index -= numbers*digits
            digits += 1
        else:
            break
    nums, digs = index / digits, index % digits
    if digits == 1:
        val = str(nums)
    else:
        val = str(pow(10, digits - 1) + nums)
    return int(val[digs])

def countOfIntegers(digits):
    a = pow(10,digits) -1
    if digits==1:
        b = 0
    else:
        b = pow(10, digits -1)
    return  a - b + 1

def test(name,index,expectValue):
    if digitAtIndex(index) == expectValue:
        print name + " is passed !"
    else:
        print digitAtIndex(index)
        print name + " is failed !"


if __name__ == "__main__":
    test("Test1", 0, 0)
    test("Test2", 1, 1)
    test("Test3", 9, 9)
    test("Test4", 10, 1)
    test("Test5", 189, 9) # 数字99的最后一位，9
    test("Test6", 190, 1) # 数字100的第一位，1
    test("Test7", 1000, 3) # 数字370的第一位，3
    test("Test8", 1001, 7) # 数字370的第二位，7
    test("Test9", 1002, 0) # 数字370的第三位，0
