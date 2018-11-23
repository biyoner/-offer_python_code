# coding= utf-8
# author:Biyoner

def Reverse(data, begin, end):
    if begin==None or end == None:
        return

    while begin<end:
        tmp = data[begin]
        data[begin] = data[end]
        data[end] = tmp
        begin += 1
        end -= 1
    return data

def LeftRotateString(string,n):
    if len(string)<=0 or n >len(string) or n<=0:
        return string

    s = list(string)
    s[0:n] = Reverse(s[0:n],0,n-1)
    s[n:] = Reverse(s[n:],0,len(string)-1-n)
    s = Reverse(s,0,len(s)-1)
    val = ""
    for i in s:
        val += i
    return val


def Test(name, s, n, expectString):
    if LeftRotateString(s,n) == expectString:
        print name + " is passed !"
    else:
        print name + " is failed !"

if __name__ == "__main__":
    Test("Test1","abcdefg",2,"cdefgab")
    Test("Test2", "abcdefg", 1, "bcdefga")
    Test("Test3", "abcdefg", 6, "gabcdef")
    Test("Test4", "", 6, "")
    Test("Test5", "abcdefg", 0, "abcdefg")
    Test("Test6", "abcdefg", 7, "abcdefg")



