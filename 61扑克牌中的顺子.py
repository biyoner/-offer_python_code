#coding = utf-8
#auther: Biyoner

def IsContinuous(numbers):
    if len(numbers) <= 0:
        return False


    numbers.sort()

    numberOfZero = 0
    numberOfGap = 0
    begin = 0


    while begin<len(numbers) and numbers[begin]==0:
        numberOfZero += 1
        begin  += 1

    end = begin + 1
    while end<len(numbers):

        if numbers[end] == numbers[begin]:
            return False

        numberOfGap += (numbers[end] - numbers[begin] - 1)

        end += 1
        begin += 1
    if numberOfGap <= numberOfZero:
        return True
    else:
        return False


def Test(name, num, expectValue):
    # print IsContinuous(num)
    if IsContinuous(num) == expectValue:
        print name + " is passed !"
    else:
        print name + " is failed !"

if __name__ == "__main__":
    Test("Test1",[1, 3, 2, 5, 4],True)
    Test("Test2", [1, 3, 2, 6, 4], False)
    Test("Test3", [0, 3, 2, 6, 4], True)
    Test("Test4", [0, 3, 1, 6, 4 ], False)
    Test("Test5", [1, 3, 0, 5, 0  ], True)
    Test("Test6", [1, 3, 0, 7, 0], False)
    Test("Test7", [1, 0, 0, 5, 0 ], True)
    Test("Test8", [1, 0, 0, 7, 0], False)
    Test("Test9", [ 3, 0, 0, 0, 0], True)
    Test("Test10", [0, 0, 0, 0, 0 ], True)
    Test("Test11", [1, 0, 0, 1, 0 ], False)
    Test("Test12", [], False)