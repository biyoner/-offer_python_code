#coding=utf-8
# author:Biyoner
### Method 1
def print1ToN1(n):
    if n<=0:
        print 0
        return 0
    number = ["0"] *(n+1)
    while not simulateADD(number):
        PrintValue(number)
def simulateADD(number):
    isOverflow = False
    l = len(number)
    for i in range(l-1,-1,-1):
        if int(number[i])<9:
            number[i] = str(int(number[i])+1)
            break
        else:
            number[i] = '0'
    if number[0] == '1':
        isOverflow = True
    return isOverflow
def PrintValue(val):
    l = len(val)
    s = ""
    for i in range(l):
        if str(val[i]) != "0":
            break
    for item in val[i:]:
        s += str(item)
    print s


### Method 2
def print1ToN2(n):
    if n<=0:
        print 0
        return 0
    number = ["0"]*(n)
    PrintValueRecursive(number,0)
    # for i in range(n):
    #     print PrintValueRecursive(number)

def PrintValueRecursive(number,index):
    if index == len(number):
        PrintValue(number)
        return
    for i in range(10):
        number[index] = i
        PrintValueRecursive(number,index+1)



### Method3 for python
def print1ToN_python(n):
    maxNum = 0
    for i  in range(n):
        maxNum = maxNum*10 + 9
    print maxNum
    count = 0
    while count<maxNum:
        count += 1
        print count



if __name__  == "__main__":
    print "test1"
    print1ToN1(3)
    print "test2"
    print1ToN2(4)
    # print1ToN_python(10)