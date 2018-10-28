# coding=utf-8
# author:Biyoner
### Method 1
###分类：
# 两个均为正数
# 一正一负
# 两个都是负数
def addTwoNum(n1,n2):
    isChange = False
    if n1<=0 and n2<=0:
        isChange = True
        result= simulateADD(-n1, -n2)
    else:
        result = simulateADD(n1, n2)
    PrintValue(result,isChange)

def simulateADD(number1,number2):
    number1 = changeNum(number1)
    number2 = changeNum(number2)
    new = ["0"] * (max(len(number1), len(number2))+1)
    for i in range(len(new)-1):
        if i >len(number1)-1:
            val1 = 0
            val2 = int(number2[i])
        elif i >len(number2)-1:
            val1 = int(number1[i])
            val2 = 0
        else:
            val1 = int(number1[i])
            val2 = int(number2[i])
        if val1 + val2 + int(new[i]) >9:
            new[i] = str(val1 + val2 + int(new[i]) - 10)
            new[i + 1] = str(int(new[i + 1]) + 1)
        elif val1 + val2 + int(new[i]) <0:
            new[i] = str(val1 + val2 + int(new[i]) + 10)
            new[i + 1] = str(int(new[i + 1]) - 1)
        else:
            new[i] = str(int(new[i])+val1+val2)

    return new

def changeNum(n):
    if n>=0:
        flag = 1
    else:
        flag = -1
    number =[]
    n = str(n*flag)
    for i in range(1,len(n)+1):
        number.append(str(int(n[-i])*flag))
    return number

def PrintValue(val,isChange):
    val.reverse()
    l = len(val)
    s = ""
    for i in range(l):
        if str(val[i]) != "0":
            break
    for item in val[i:]:
        s += str(item)
    if isChange:
        s = "-"+s
    print s

if __name__ == "__main__":
    addTwoNum(2000,-4)
