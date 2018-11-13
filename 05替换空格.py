# coding=utf-8
# author:Biyoner

def replace1(s1,s2):
    #与书上方法相同，但是产生了新的数组，牺牲了空间复杂度
    cal = 0
    s1 = list(s1)
    for s in s1:
        if s == ' ':
            cal += 1
    all = len(s1) + cal*2
    new_s = [None] * all
    for j in range(len(s1)):
        if s1[len(s1)-j-1]!= ' ':
            all -= 1
            new_s[all] = s1[len(s1)-j-1]
        else:
            all -= 1
            new_s[all] = "0"
            all -= 1
            new_s[all] = "2"
            all -= 1
            new_s[all] = "%"
    new_s =''.join(map(str,new_s))
    return new_s

def replace2(s1,s2):
    # 同样因为产生了新的数组，牺牲了空间复杂度
    s1 = list(s1)
    new_s = []
    for item in s1:
        if item != ' ':
            new_s.append(item)
        else:
            new_s.append("%20")
    new_s = ''.join(map(str, new_s))
    return new_s

def replace3(s1,s2):
    new_s = s1.replace(" ",s2)
    return new_s

if __name__ == "__main__":
    s1 = "hello world"
    s2 = " helloworld"
    s3 = "helloworld "
    s4 = "hello  world"
    s5 = ""
    s6 = " "
    s7 = "helloworld"
    s8 =  "   "
    ss = [s1,s2,s3,s4,s5,s6,s7,s8]
    for s in ss:
        r = "%20"
        new1 = replace1(s,r)
        print new1
        new2 = replace2(s,r)
        print new2
        new3 = replace3(s,r)
        print new3
