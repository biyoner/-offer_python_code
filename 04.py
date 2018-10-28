# coding=utf-8
# author:Biyoner
def find_2d_arrary(L, val):
    flag = False
    if L == []:
        return flag
    if L[0] == []:
        return flag
    cols = len(L)
    rows = len(L[0])
    right_top = L[0][rows-1]
    if right_top == val:
        flag = True
        return flag
    elif right_top> val:
        new_array = [item[0:rows-1] for item in L]
        return find_2d_arrary(new_array,val)
    else:
        new_array = L[1:cols]
        return find_2d_arrary(new_array,val)

if __name__ == "__main__":
    L1 = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    L2 = []
    #######################
    find = [7,5,1,15,0,16]
    for item in find:
        result = find_2d_arrary(L1,item)
        print result
    #######################
    result = find_2d_arrary(L2,1)
    print result