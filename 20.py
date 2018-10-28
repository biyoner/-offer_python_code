# coding=utf-8
# author:Biyoner
def isNumeric(ch):
    if ch == "":
        return False
    ch,interger = scanInteger(ch)

    if ch != "" and ch[0] ==".":
        ch = ch[1:]
        ch, _ = scanUsnsignedInteger(ch)
        interger = _ or interger
    if ch != "" and (ch[0] == "E" or ch[0] =="e"):
        ch = ch[1:]
        ch, _ = scanInteger(ch)
        interger = _ and interger
    if ch == "" and interger:
        return True
    else:
        return False



def scanInteger(ch):
    if ch == "":
        return ch,False
    else:
        if ch[0] == "+" or ch[0] == "-":
            ch = ch[1:]
        ch, interger = scanUsnsignedInteger(ch)
        return ch, interger

def scanUsnsignedInteger(ch):
    before = len(ch)
    while len(ch)>0 and ch[0]>="0" and ch[0]<="9":
        ch = ch[1:]
    return ch,len(ch)<before

def Test(name,ch,result):
    if isNumeric(ch) == result:
        print name + " " + "passed !"
    else:
        print name + " " + "failed !"

if __name__ == "__main__":
    Test("Test1", "100", True)
    Test("Test2", "123.45e+6", True)
    Test("Test3", "+500", True)
    Test("Test4", "5e2", True)
    Test("Test5", "3.1416", True)
    Test("Test6", "600.", True)
    Test("Test7", "-.123", True)
    Test("Test8", "-1E-16", True)
    Test("Test9", "1.79769313486232E+308", True)

    Test("Test10", "12e", False)
    Test("Test11", "1a3.14", False)
    Test("Test12", "1+23", False)
    Test("Test13", "1.2.3", False)
    Test("Test14", "+-5", False)
    Test("Test15", "12e+5.4", False)
    Test("Test16", ".", False)
    Test("Test17", ".e1", False)
    Test("Test18", "e1", False)
    Test("Test19", "+.", False)
    Test("Test20", "", False)

