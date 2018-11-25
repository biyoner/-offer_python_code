# coding=utf-8
# author:Biyoner

# 代码里的将一个数对0x100000000取模（注意：Python的取模运算结果恒为非负数），
# 是希望该数的二进制表示从第32位开始到更高的位都同是0（最低位是第0位），
# 以在0-31位上模拟一个32位的int。

def Add(n1,n2):
    sum1 = (n1^n2) % 0x100000000
    sum2 = ((n1&n2)<<1) % 0x100000000

    if sum2 != 0:
        return Add(sum1,sum2)

    return sum1 if sum1<=0x7FFFFFFF else sum1 |(~0x100000000+1)

def Test(name,num1,num2,expect):
    if Add(num1,num2) == expect:
        print name + " is passed !"
    else:
        print name + " is failed !"

if __name__ == "__main__":
    Test("Test1",1, 2, 3)
    Test("Test2",111, 899, 1010)
    Test("Test3",-1, 2, 1)
    Test("Test4",1, -2, -1)
    Test("Test5",3, 0, 3)
    Test("Test6",0, -4, -4)
    Test("Test7",-2, -8, -10)
