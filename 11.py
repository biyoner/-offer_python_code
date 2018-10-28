# coding=utf-8
# author:Biyoner
def find_rotate(L):
    if len(L) == 0:
        return "Invalid list"
    left = 0
    right = len(L)-1
    center = (left + right)/2
    if L[left] == L[right]:
        min_val = 100
        for i in range(len(L)):
            if L[i]<min_val:
                min_val = L[i]
        return min_val
    elif L[left] < L[right]:
        return L[0]
    else:
        while center!=left and center!= right:
            if L[center]>=L[left]:
                left = center
            else:
                right = center
            center = (left + right) / 2
        return min(L[left],L[right])
if __name__ == "__main__":
    L = [1,2,3,4,5]
    print find_rotate(L)
