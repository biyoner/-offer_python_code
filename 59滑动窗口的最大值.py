#coding = utf-8
#auther: Biyoner

from collections import deque

def maxInWindows(num,size):
    maxWindows = []

    if len(num)<=0 or size>len(num) or size<=0:
        return maxWindows

    index = deque()


    for i in range(len(num)):
        if len(index)<=0:
            index.append(i)
        else:
            if num[index[0]] < num[i]:
                index.clear()
                index.append(i)
            else:
                if i - index[0] >= size:
                    index.popleft()

                for j in range(len(index)):
                    if num[index[j]] < num[i]:
                        for _ in range(len(index) - j):
                            index.pop()
                        break
                index.append(i)
        if len(index)>0 and i>=size-1:
            maxWindows.append(num[index[0]])
    # print maxWindows
    return maxWindows

def Test(name, data, size, expect):
    if maxInWindows(data,size) == expect:
        print name + " is passed !"
    else:
        print name + " is failed !"

if __name__  == "__main__":
    Test("Test1",[2,3,4,2,6,2,5,1],3,[ 4, 4, 6, 6, 6, 5 ])
    Test("Test2", [1, 3, -1, -3, 5, 3, 6, 7 ], 3, [3, 3, 5, 5, 6, 7])
    Test("Test3", [1, 3, 5, 7, 9, 11, 13, 15], 4, [7, 9, 11, 13, 15 ])
    Test("Test4", [16, 14, 12, 10, 8, 6, 4], 5, [16, 14, 12])
    Test("Test5", [10, 14, 12, 11], 1, [10, 14, 12, 11])
    Test("Test6", [10, 14, 12, 11], 4, [14])
    Test("Test7", [10, 14, 12, 11], 0, [])
    Test("Test8", [10, 14, 12, 11], 5, [])
    Test("Test9", [], 5, [])
