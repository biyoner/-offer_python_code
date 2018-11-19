#coding= utf-8
#author:Biyoner

import collections
def FirstNotRepeatingChar(string):
    if len(string)<=0:
        return ""

    dic = collections.OrderedDict()
    for ch in string:
        if dic.has_key(ch):
            dic[ch] += 1
        else:
            dic[ch] = 1

    val = ""

    for key in dic.keys():
        if dic[key] == 1:
            val = key
            break

    return val

def Test(name, string, expectedValue):
    if FirstNotRepeatingChar(string) == expectedValue:
        print name + " is passed !"
    else:
        print name + " is failed !"

if __name__ == "__main__":

    Test("Test1","google", "l")

    Test("Test2","aabccdbd", "")


    Test("Test3","abcdefg", 'a')


    Test("Test4","", "")
