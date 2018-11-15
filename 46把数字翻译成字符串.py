#coding= utf-8
#author:Biyoner

def GetTranslationCount(number):
    if int(number)<0:
        return 0

    i = len(number)-1
    li = []
    li_1 = []
    li_2 = []
    while i>=0:

        val = chr(ord("a") + int(number[i]))
        if len(li_1)>0:
            for item in li_1:
                li.append(val+item)
        else:
            li.append(val)

        if len(li_1)>0 and (number[i]+number[i+1] >= '10' ) and (number[i]+number[i+1]<='25'):
            val = chr(ord("a") + int(number[i]+number[i+1]))
            if len(li_2)>0:
                for item in li_2:
                    li.append(val+item)
            else:
                li.append(val)
        # print li
        i-= 1
        li_2 = li_1
        li_1 = li
        li = []
    return len(li_1)


def Test(name,number,expectedValue):
    if GetTranslationCount(str(number)) == expectedValue:
        print name + " is passed !"
    else:
        print name + " is failed !"


if __name__ == "__main__":
    Test("Test1", 0, 1)
    Test("Test2", 10, 2)
    Test("Test3", 125, 3)
    Test("Test4", 126, 2)
    Test("Test5", 426, 1)
    Test("Test6", 100, 2)
    Test("Test7", 101, 2)
    Test("Test8", 12258, 5)
    Test("Test9", -100, 0)