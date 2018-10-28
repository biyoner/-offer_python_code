#coding=utf-8
#在此类运算中，直接将数字转成二进制，不用过多考虑
# author:Biyoner
def NumberOf1(n):
    count = 0
    flag = 1
    if n <0:
        print "<0"
        n *= -1
        count = 1
    while flag and flag<=n:
        if flag & n:
            count += 1
        flag = flag<<1
    return count

def NumberOf2(n):
    count = 0
    if n <0:
        n *= -1
        count = 1

    while(n):
        n = n&(n-1)
        count += 1
    return count

def test(li):
    if li[1] == NumberOf1(li[0]):
    #if li[1] == NumberOf2(li[0]):
        return "Test passed"
    else:
        return "Test failed"

if __name__ == "__main__":
    #print NumberOf1(-8)
    tests = [[0, 0],[1, 1],[10, 2],[int(0x7FFFFFFF), 31],[int(0xFFFFFFFF), 32],[int(0x80000000), 1]]
    for item in tests:
        print test(item)

