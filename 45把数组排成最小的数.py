#coding= utf-8
#author:Biyoner


def PrintMinNumber(numbers):
    if len(numbers) <= 0:
        return 0
    if len(numbers) == 1:
        return str(numbers[0])
    l = qSort(numbers,0,len(numbers)-1)
    val = ""
    for i in l:
        val += str(i)
    return val


def qSort(numbers,start,end):
    if start >= end:
        return
    base = numbers[start]
    i = start
    j = end
    while i<j:
        while compare(numbers[j],base) and i<j:
            j -= 1
        swap(numbers,i,j)
        while compare(base,numbers[i]) and i<j:
            i += 1
        swap(numbers,i,j)
    qSort(numbers,start,i-1)
    qSort(numbers,i+1,end)
    return numbers


def swap(numbers,i,j):
    tmp = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = tmp


def compare(number1,number2):
    combine1 = str(number1)+str(number2)
    combine2 = str(number2)+str(number1)
    if combine1 >= combine2:
        return True
    else:
        return False


def Test(name,number,expectedValue):
    if PrintMinNumber(number) == expectedValue:
        print name + " is passed !"
    else:
        print name + " is failed !"

if __name__ == "__main__":
    Test("Test1", [3, 5, 1, 4, 2], "12345")
    Test("Test2",[3, 32, 321], "321323")
    Test("Test3", [3, 323, 32123], "321233233")
    Test("Test4", [1, 11, 111], "111111")
    Test("Test5", [321], "321")
    Test("Test6", [], 0)