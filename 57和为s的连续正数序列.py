# coding= utf-8
# author:Biyoner

def FindContinuousSequence(s):
    if s < 3:
        return None

    begin = 1
    end = 2
    curSum = begin + end

    l = []
    while begin < (s+1)//2:
        if curSum < s:
            end += 1
            curSum += end
        elif curSum >s:
            curSum -= begin
            begin += 1
        else:
            l.append([begin,end])
            end += 1
            curSum += end
    return l

def Test(name,num):
    print "%s for %d begins:" % (name,num)
    l = FindContinuousSequence(num)
    if l == None:
        print l
    else:
        for r in l:
            for i in range(r[0],r[1]+1):
                print i,
            print " "

if __name__ == "__main__":
    Test("test1", 1)
    Test("test2", 3)
    Test("test3", 4)
    Test("test4", 9)
    Test("test5", 15)
    Test("test6", 100)

