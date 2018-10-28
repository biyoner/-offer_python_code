# coding=utf-8
# author:Biyoner

def insert_list(l1,l2):
    len1 = len(l1)
    len2 = len(l2)
    new_list = [None]*(len1+len2)
    i = len1-1
    j = len2-1
    for k in range(len1 + len2):
        if i<0:
            val1 = -1
        else:
            val1 = l1[i]
        if j < 0:
            val2 = -1
        else:
            val2 = l2[j]

        if val1 < val2 :
            new_list[-k-1] = val2
            j -= 1
        else:
            new_list[-k-1] = val1
            i -= 1
    return new_list





if __name__ == "__main__":
    L1 = [1,3,5,7,8,9]
    L2 = [2,4,6]
    print insert_list(L1,L2)