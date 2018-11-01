#coding= utf-8
#author:Biyoner

def IsPopOrder(l1,l2):
    #l1是压入栈的顺序
    #l2是出栈的顺序

    bPossoble = False
    if len(l1) != len(l2) or len(l1)<=0 or len(l2)<=0:
        return bPossoble

    stack = []
    while len(l1)>0 or (len(stack) > 0 and stack[-1] == l2[0]):
        if len(stack) > 0 and stack[-1] == l2[0]:
            l2 = l2[1:]
            stack.pop()
        else:
            stack.append(l1[0])
            l1 = l1[1:]
        # print l1, l2,stack

    if len(l2) == 0:
        bPossoble = True
    return bPossoble

def Test(name,l1,l2,result):
    if IsPopOrder(l1,l2) == result:
        print name+ " " + "is passed !"
    else:
        print name + " " + "is failed !"

if __name__ == "__main__":
    Test("Test1",[1, 2, 3, 4, 5],[4, 5, 3, 2, 1],True)
    Test("Test2", [1, 2, 3, 4, 5], [3, 5, 4, 2, 1], True)
    Test("Test3", [1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False)
    Test("Test4", [1, 2, 3, 4, 5], [3, 5, 4, 1, 2], False)
    Test("Test5", [1], [2], False)
    Test("Test6", [1], [1], True)
    Test("Test7", [], [], False)
