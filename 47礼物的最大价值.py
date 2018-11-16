#coding= utf-8
#author:Biyoner

def getMaxValue1(gifts):
    rows = len(gifts)
    if rows<=0:
        return None

    cols = len(gifts[0])
    if cols<=0:
        return None

    maxValues = []

    for i in range(rows):
        maxValues.append([])
        for j in range(cols):
            up = 0
            left = 0
            if i>0:
                up = maxValues[i-1][j]
            if j>0:
                left = maxValues[i][j-1]

            maxValues[i].append(max(up,left) + gifts[i][j])
    return maxValues[rows-1][cols-1]

def getMaxValue2(gifts):
    rows = len(gifts)
    if rows <= 0:
        return None

    cols = len(gifts[0])
    if cols <= 0:
        return None

    maxValues = []

    for i in range(rows):
        for j in range(cols):
            up = 0
            left = 0
            if i>0:
                up = maxValues[j]
            if j>0:

                left = maxValues[j-1]
            if len(maxValues) >= cols:
                maxValues[j] = max(up, left) + gifts[i][j]
            else:
                maxValues.append(max(up, left) + gifts[i][j])

    return maxValues[cols-1]
def Test(names,values,expectedValue):
    if getMaxValue1(values) == expectedValue:
        print names + " is passed !"
    else:
        print names + " is failed !"

if __name__ == "__main__":
    Test("Test1",[[1,2,3],[4,5,6],[7,8,9]],29)
    Test("Test2", [[1,10,3,8],[12,2,9,6],[5,7,4,11],[3,7,16,5]], 53)
    Test("Test3", [[1, 10, 3, 8]], 22)
    Test("Test4", [[1],[12],[5],[3]], 21)
    Test("Test5", [[3]], 3)
    Test("Test6", [[]], None)
