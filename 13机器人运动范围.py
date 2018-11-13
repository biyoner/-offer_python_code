# coding=utf-8
# author:Biyoner
def robot_move(cols,rows,threshold):
    init = [0,0]
    mark = [[0 for _ in range(rows)] for _ in range(cols)]
    all =hasPathCore(cols,rows,mark,threshold,init)
    return all


def  hasPathCore(cols,rows,mark,threshold,position):
    i,j = position[0],position[1]
    hasPath = 0
    if i>=0 and i<cols and j >=0 and j<rows and count(i)+count(j)<=threshold and mark[i][j]==0:

        mark[i][j] = 1
        hasPath = 1+ hasPathCore(cols,rows,mark,threshold,[i,j-1]) +\
                  hasPathCore(cols,rows,mark,threshold,[i,j+1]) + \
                  hasPathCore(cols, rows, mark,threshold, [i-1,j]) + \
                  hasPathCore(cols, rows, mark,threshold, [i+1,j])
    return hasPath

def count(num):
    total = 0
    while num:
        total += num%10
        num = num/10
    return total

def test(parameters):

    if robot_move(parameters[1],parameters[2],parameters[0]) == parameters[3]:
        return "Test passed"
    else:
        return "Failure"

if __name__ == "__main__":
    test1 = [5,10,10,21]
    test2 = [ 15, 20, 20, 359]
    test3 = [10, 1, 100, 29]
    test4 = [10, 1, 10, 10]
    test5 = [15, 100, 1, 79]
    test6 = [15, 10, 1, 10]
    test7 = [15, 1, 1, 1]
    test8 = [0, 1, 1, 1]
    test9 = [-10, 10, 10, 0]
    print test(test1)
    print test(test2)
    print test(test3)
    print test(test4)
    print test(test5)
    print test(test6)
    print test(test7)
    print test(test8)
    print test(test9)