#coding= utf-8
#author:Biyoner

def Combination(string):
    if len(string) == 0:
        return None
    l = list(string)
    # print combination(l,2,[])
    for i in range(1,len(l)+1):
        combination(l,i,[])


def combination(string,m,result):
    if m == 0:
        print "result","".join(result)
        return
    if len(string) != 0:
        result.append(string[0])
        combination(string[1:], m - 1, result)
        result.pop()
        combination(string[1:], m, result)


if __name__ == "__main__":
    string4 = "abc"
    Combination(string4)