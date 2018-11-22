# coding= utf-8
# author:Biyoner

def FindNumberAppearingOnce(numbers):
    if len(numbers)<=0:
        return None

    bitSum = [0 for _ in range(32)]
    for i in numbers:
        bitindex = 1
        for j in range(len(bitSum)):
            if i & bitindex:
                bitSum[j] += 1
            bitindex=bitindex<<1

    number = 0
    for bit in range(len(bitSum)-1,-1,-1):
        number = number<<1
        number += bitSum[bit]%3

    if number in numbers:
        return number
    else:
        return number-pow(2,32)



def TwoToTen(s,isPositive=True):
    if isPositive:
        return int(s,2)
    else:
        s = list(s)





def Test(name,data,expectNum):
    if FindNumberAppearingOnce(data) == expectNum:
        print name + " is passed !"
    else:
        print name + " is failed !"


if __name__ == "__main__":
    Test("Test1",[1, 1, 2, 2, 2, 1, 3 ],3)
    Test("Test2", [4, 3, 3, 2, 2, 2, 3], 4)
    Test("Test3", [4, 4, 1, 1, 1, 7, 4], 7)
    Test("Test4", [-10, 214, 214, 214], -10)
    Test("Test5", [-209, 3467, -209, -209 ], 3467)
    Test("Test6", [1024, -1025, 1024, -1025, 1024, -1025, 1023], 1023)
    Test("Test7", [-1024, -1024, -1024, -1023], -1023)
    Test("Test8", [-23, 0, 214, -23, 214, -23, 214], 0)
    Test("Test9", [0, 3467, 0, 0, 0, 0, 0, 0], 3467)
