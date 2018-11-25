# coding = utf-8
# author: Biyoner

def MaxDiff(numbers):
    if len(numbers)<=0:
        return 0

    minimum = 10000
    maxDiff = -1000
    for i in range(len(numbers)):
        if i>0 and numbers[i-1] < minimum:
            minimum = numbers[i-1]
        if numbers[i] - minimum > maxDiff:
            maxDiff = numbers[i] - minimum
        
    # print maxDiff
    return maxDiff
def Test(name, number, expectValue):
    if MaxDiff(number) == expectValue:
        print name + " is passed !"
    else:
        print name + " is failed !"

if __name__ == "__main__":
    Test("Test1",[4, 1, 3, 2, 5], 4)
    Test("Test2", [ 1, 2, 4, 7, 11, 16], 15)
    Test("Test3", [16, 11, 7, 4, 2, 1], -1)
    Test("Test4", [16, 16, 16, 16, 16], 0)
    Test("Test5", [9, 11, 5, 7, 16, 1, 4, 2 ], 11)
    Test("Test6", [2, 4], 2)
    Test("Test7", [4,2], -2)
    Test("Test8", [], 0)
