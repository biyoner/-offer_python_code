# coding= utf-8
# author:Biyoner

def FindNumsAppearOnce(data):
    if len(data)<=0:
        return None

    resultExclusiveOR = data[0]
    for i in range(1,len(data)):
        resultExclusiveOR ^= data[i]

    indexOf1 = FindFirstBitIs1(resultExclusiveOR)
    num1 = 0
    num2 = 0
    for i in data:
        # if i & pow(2,indexOf1):
        if (i>>indexOf1) & 1:
            num1 = num1 ^i
        else:
            num2 = num2 ^ i
    return num1,num2


def FindFirstBitIs1(num):
    indexBit = 0
    while 1:

        if num&1 == 1:
            break
        else:
            num = num>>1
        indexBit += 1

    return indexBit

def Test(name,data,expectNum1,expectNum2):
    num1,num2 = FindNumsAppearOnce(data)
    if (num1== expectNum1 and num2==expectNum2) or (num1== expectNum2 and num2==expectNum1) :
        print name + " is passed !"
    else:
        print name + " is failed !"

if __name__ == "__main__":
   Test("Test1",[ 2, 4, 3, 6, 3, 2, 5, 5 ],4,6)
   Test("Test2", [4,6], 4, 6)
   Test("Test3", [ 4, 6, 1, 1, 1, 1], 4, 6)


