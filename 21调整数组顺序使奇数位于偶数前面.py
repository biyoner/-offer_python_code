# coding=utf-8
# author:Biyoner
global_flag = False
def judgeNumber(n):
    return (n&1) == 0


def reOrder(L):
    l = len(L)
    begin = 0
    end = l-1
    while begin < end:

        if judgeNumber(L[begin]) and (not judgeNumber(L[end])):
            temp = L[begin]
            L[begin] = L[end]
            L[end] = temp

        if not judgeNumber(L[begin]):
            begin += 1

        if judgeNumber(L[end]):
            end -= 1
    return L


if __name__ == "__main__":
    tests = [[1, 2, 3, 4, 5, 6, 7],[2, 4, 6, 1, 3, 5, 7],[1, 3, 5, 7, 2, 4, 6],[1],[2],[]]
    for item in tests:
        print reOrder(item)