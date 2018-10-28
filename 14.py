# coding=utf-8
# author:Biyoner

def maxProduct_dp (length):
    ### init length
    if length<2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    product = [0 for _ in range(length+1)]
    product[0] = 0
    product[1] = 1
    product[2] = 2
    product[3] = 3
    for i in range(4,length+1):
        maxP = 0
        for j in range(1,i/2+1):
            if product[j] * product[i-j] > maxP:
                maxP = product[j] *product[i-j]
        product[i] = maxP
    return product[length]


def maxProduct_greedy(length):
    if length<2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    product = [0,1,2,3]

    maxP = 1
    while length>=4:
        if length >= 5:
            length = length - 3
            maxP *= 3
        if length == 4:
            maxP *= 4
            length = length - 4
    if length:
        maxP *= product[length]

    return maxP
def test(li):
    if maxProduct_dp(li[0]) == li[1] and maxProduct_greedy(li[0]) == li[1]:
        return "Both are right"
    if maxProduct_dp(li[0]) != li[1]:
        return "DP is wrong"
    if maxProduct_greedy(li[0]) != li[1]:
        return "Greedy is wrong"


if __name__ == "__main__":
    print "test1 " +test([1,0])
    print "test2 " + test([2,1])
    print "test3 " +test([3,2])
    print "test4 " +test([4,4])
    print "test5 " + test([5,6])
    print "test6 " + test([6,9])
    print "test7 " + test([7,12])
    print "test8 " + test([8,18])
    print "test9 " + test([9,27])
    print "test10 " + test([10,36])
    print "test11 " + test([50,86093442])

