# coding=utf-8
# author:Biyoner

def multiply(numbers):
    B = []

    if len(numbers)<=0:
        return 0

    for i in range(len(numbers)):
        B.append([])
        for j in range(len(numbers)):
            if i == j:
                B[i].append(1)
            else:
                B[i].append(numbers[j])

    val = []

    for i in range(len(B)):
        mul = 1
        for j in B[i]:
            mul *= j
        val.append(mul)

    return val

def Test(name, number, expect):
    if multiply(number) == expect:
        print name + " is passed !"
    else:
        print name + " is failed !"

if __name__ == "__main__":
    Test("Test1", [1, 2, 3, 4, 5 ], [120, 60, 40, 30, 24])
    Test("Test2", [1, 2, 0, 4, 5], [0, 0, 40, 0, 0 ])
    Test("Test3", [1, 2, 0, 4, 0], [ 0, 0, 0, 0, 0])
    Test("Test4", [1, -2, 3, -4, 5], [120, -60, 40, -30, 24])
    Test("Test5", [ 1, -2 ], [-2, 1 ])