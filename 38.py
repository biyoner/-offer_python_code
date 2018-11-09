#coding= utf-8
#author:Biyoner
import copy
def Permutation(string):
    if len(string) == 0:
        return None
    l = list(string)
    result = []
    for item in permutation(l,0):
        result.append("".join(item))
    return result


def permutation(string,begin):
    result = []
    if begin == len(string):
        return [string]
    for i in range(begin,len(string)):
        new = copy.copy(string)
        temp =new[i]
        new[i] = new[begin]
        new[begin] = temp
        result=result+permutation(new, begin+1)
    return result



if __name__ == "__main__":
    string1 = ""
    string2 = "a"
    string3 = "ab"
    string4 = "abc"
    print Permutation(string1)
    print Permutation(string2)
    print Permutation(string3)
    print Permutation(string4)