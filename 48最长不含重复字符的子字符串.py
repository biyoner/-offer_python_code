#coding= utf-8
#author:Biyoner

def longestSubstringWithoutDuplication(string):
    if len(string) <= 0:
        return 0

    dic = {}
    for i in range(26):
        dic[chr(ord("a")+i)] = -1
    maxLength = 0
    # maxString = ""
    curLength = 0
    for i in range(len(string)):
        # print string[i]
        if dic[string[i]] <0:
            curLength+= 1
            # maxString += string[i]
            dic[string[i]] = i
        else:
            if i-dic[string[i]] <= curLength :
                curLength = i - dic[string[i]]
            else:
                curLength += 1
            dic[string[i]] = i
        if curLength > maxLength:
            maxLength = curLength
        # print maxLength

    return maxLength

def Test(name, string, expectedValue):
    if longestSubstringWithoutDuplication(string) == expectedValue:
        print name + " is passed !"
    else:
        print name + " is failed !"

if __name__ == "__main__":
    Test("Test1","abcacfrar",4)
    Test("Test2", "acfrarabc", 4)
    Test("Test3", "arabcacfr", 4)
    Test("Test4", "aaaa", 1)
    Test("Test5", "abcdefg", 7)
    Test("Test6", "aaabbbccc", 2)
    Test("Test7", "abcdcba", 4)
    Test("Test8", "abcdaef", 6)
    Test("Test9", "a", 1)
    Test("Test10", "", 0)