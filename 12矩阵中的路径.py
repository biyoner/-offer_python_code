# coding=utf-8
# author:Biyoner
def recall(array,string):
    cols = len(array)
    rows = len(array[0])
    mark = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(cols):
        for j in range(rows):
            if array[i][j] == string[0]:
                init_position = [i,j]
                result = hasPathCore(array,mark,string,init_position)
                return result

def hasPathCore(array,mark,string,position,string_len=0):
    ### official version
    i, j = position[0], position[1]
    if string_len == len(string):
        return True
    hasPath = False
    if i>=0 and i<len(array) and j >=0 and j <len(array[0]) and array[i][j] == string[string_len] and mark[i][j]==0:
        string_len += 1
        mark[i][j] = 1
        hasPath = hasPathCore(array,mark,string,[i,j-1],string_len) or \
                hasPathCore(array,mark,string,[i,j+1],string_len) or \
                hasPathCore(array,mark,string,[i-1,j],string_len) or \
                hasPathCore(array,mark,string,[i+1,j],string_len)
        if not hasPath:
            string_len -= 1
            mark[i][j] = 0
    return hasPath

if __name__ == "__main__":
    matrix = [['a','b','t','g'],['c','f','c','j'],['j','d','e','h']]
    string = "bfcjh"
    print recall(matrix,string)

