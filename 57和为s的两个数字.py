# coding= utf-8
# author:Biyoner

def FindNumbersWithSum(data,Sum):
    flag = False

    if len(data)<=0:
        return flag,-1,-1

    begin = 0
    end = len(data)-1
    while end>begin:
        if data[begin] + data[end] > Sum:
            end -= 1
        elif data[begin] + data[end] < Sum:
            begin += 1
        else:
            flag = True
            break

    return flag,data[begin],data[end]

def Test(name, data, s, expectF):
    f,n1,n2 = FindNumbersWithSum(data,s)
    if f == expectF:
        print name + "is passed ! The two numbers are %d and %d" % (n1,n2)
    else:
        print name + "is failed !"

if __name__ == "__main__":
    Test("Test1", [1, 2, 4, 7, 11, 15], 15, True)
    Test("Test2", [1, 2, 4, 7, 11, 16], 17, True)
    Test("Test3", [1, 2, 4, 7, 11, 16], 10, False)
    Test("Test4", [], 0, False)