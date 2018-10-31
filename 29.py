#coding= utf-8
#author:Biyoner
def PrintMatrixClockwisely(numbers):
    columns = len(numbers)
    rows = len(numbers[0])
    start = 0
    val = []
    while columns>start*2 and rows>start*2:
        val = val + PrintMatrixInCircle(numbers,columns,rows,start)
        start+= 1
    return val

def PrintMatrixInCircle(numbers,  rows, columns, start):
    endX = columns -1 - start
    endY = rows -1 - start
    result = []

    for i in range(start, endX):
        number = numbers[start][i]
        result.append(number)

    if start == endY:
        number = numbers[start][endX]
        result.append(number)
    if start < endY:
        for i in range(start, endY):
            number = numbers[i][endX]
            result.append(number)

    if start == endX and endX!= endY:
        number = numbers[endY][endX]
        result.append(number)
    if start< endX and start< endY:
        for i in range(endX, start, -1):
            number = numbers[endY][i]
            result.append(number)

    if start <= endY-1 and start<=endX-1:
        for i in range(endY, start, -1):
            number = numbers[i][start]
            result.append(number)
    return result

def Test(name, col,row,result):
    if col<=0 or row<=0:
        return False
    numbers = []
    count = 1
    for i in range(row):
        line = []
        for j in range(col):
            line.append(count)
            count += 1
        numbers.append(line)
    val = PrintMatrixClockwisely(numbers)
    if val == result:
        print name+ " " + "is passed !"
    else:
        print name + " " + "is failed !"



if __name__ == "__main__":
    #1
    Test("Test1",1, 1,[1])

    #1 2
    #3 4
    Test("Test2", 2, 2, [1,2,4,3])

    #1 2 3 4
    #5 6 7 8
    #9 10 11 12
    #13 14 15 16
    Test("Test3", 4, 4, [1, 2, 3, 4,8,12,16,15,14,13,9,5,6,7,11,10])

    #1 2 3 4 5
    #6 7 8 9 10
    #11 12 13 14 15
    #16 17 18 19 20
    #21 22 23 24 25
    Test("Test4", 5, 5, [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6,7,8,9,14,19,18,17,12,13])

    #1
    #2
    #3
    #4
    #5
    Test("Test5", 1, 5, [1, 2, 3, 4, 5])

    #1 2
    #3 4
    #5 6
    #7 8
    #9 10
    Test("Test6", 2, 5, [1, 2, 4, 6,8,10,9,7,5,3])

    #1 2 3
    #4 5 6
    #7 8 9
    #10 11 12
    #13 14 15
    Test("Test7", 3, 5, [1,2,3,6,9,12,15,14,13,10,7,4,5,8,11])

    #1 2 3 4
    #5 6 7 8
    #9 10 11 12
    #13 14 15 16
    #17 18 19 20
    Test("Test8", 4, 5, [1, 2, 3,4,8,12,16,20,19,18,17,13,9,5,6,7,11,15,14,10])

    #1 2 3 4 5
    Test("Test9", 5, 1, [1, 2, 3, 4,5])


    #1 2 3 4 5
    #6 7 8 9 10
    Test("Test10", 5, 2, [1, 2, 3, 4, 5,10,9,8,7,6])


    #1 2 3 4 5
    #6 7 8 9 10
    #11 12 13 14 15
    Test("Test11", 5, 3, [1, 2, 3, 4, 5, 10,15,14,13,12,11,6,7,8,9])

    # 1 2 3 4 5
    # 6 7 8 9 10
    # 11 12 13 14 15
    #16 17 18 19 20
    Test("Test12", 5, 4, [1, 2, 3, 4, 5, 10, 15, 20,19,18,17,16,11,6,7,8,9,14,13,12])


