#coding= utf-8
#author:Biyoner

def NumberOf1Between1AndN(n):
    if n <= 0:
        return 0
    val = NumberOf1(str(n))
    return val

def NumberOf1(n):
    # print n
    first = int(n[0])
    length = len(n)
    if  length==1 and first== 0:
        return 0
    if length==1 and first>0:
        return 1
    numFirstDigit = 0
    if first >1:
        numFirstDigit = pow(10,length-1)
    elif first== 1:
        numFirstDigit = int(n[1:])+1

    numOtherDigits = first * (length-1) * pow(10,(length-2))
    numRecursive = NumberOf1(n[1:])
    # print numFirstDigit,numOtherDigits,numRecursive
    return numFirstDigit + numOtherDigits + numRecursive

def Test(name,n,expectedResult):
    if NumberOf1Between1AndN(n) == expectedResult:
        print name + " is passed !"
    else:
        print name + " is failed !"


if __name__ == "__main__":
    Test("Test1", 1, 1)
    Test("Test2", 5, 1)
    Test("Test3", 10, 2)
    Test("Test4", 55, 16)
    Test("Test5", 99, 20)
    Test("Test6", 10000, 4001)
    Test("Test7", 21345, 18821)
    Test("Test8", 0, 0)