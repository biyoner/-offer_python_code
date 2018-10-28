# coding=utf-8
# author:Biyoner
def regularExpressCore(ch, pattern):
    # print ch,pattern
    if ch=="" and pattern=="":
        return True
    if ch!="" and pattern=="":
        return False

    if len(pattern)>1 and pattern[1] == "*":
        if len(ch) > 0 and (pattern[0] == "." or pattern[0] == ch[0]):
            return regularExpressCore(ch,pattern[2:]) or regularExpressCore(ch[1:],pattern) or regularExpressCore(ch[1:],pattern[2:])
        else:
            return regularExpressCore(ch,pattern[2:])

    if len(ch)>0 and (pattern[0] == "." or pattern[0]==ch[0]):
        return regularExpressCore(ch[1:],pattern[1:])

    return False




def Test(name,ch,pattern,result):
    if regularExpressCore(ch,pattern) == result:
        print name + " " + "passed !"
    else:
        print name + " " + "failed !"



if __name__ == "__main__":
    Test("Test01", "", "", True)
    Test("Test02", "", ".*", True)
    Test("Test03", "", ".", False)
    Test("Test04", "", "c*", True)
    Test("Test05", "a", ".*", True)
    Test("Test06", "a", "a.", False)
    Test("Test07", "a", "", False)
    Test("Test08", "a", ".", True)
    Test("Test09", "a", "ab*", True)
    Test("Test10", "a", "ab*a", False)
    Test("Test11", "aa", "aa", True)
    Test("Test12", "aa", "a*", True)
    Test("Test13", "aa", ".*", True)
    Test("Test14", "aa", ".", False)
    Test("Test15", "ab", ".*", True)
    Test("Test16", "ab", ".*", True)
    Test("Test17", "aaa", "aa*", True)
    Test("Test18", "aaa", "aa.a", False)
    Test("Test19", "aaa", "a.a", True)
    Test("Test20", "aaa", ".a", False)
    Test("Test21", "aaa", "a*a", True)
    Test("Test22", "aaa", "ab*a", False)
    Test("Test23", "aaa", "ab*ac*a", True)
    Test("Test24", "aaa", "ab*a*c*a", True)
    Test("Test25", "aaa", ".*", True)
    Test("Test26", "aab", "c*a*b", True)
    Test("Test27", "aaca", "ab*a*c*a", True)
    Test("Test28", "aaba", "ab*a*c*a", False)
    Test("Test29", "bbbba", ".*a*a", True)
    Test("Test30", "bcbbabab", ".*a*a", False)

    # print regularExpressCore("", ".*")






