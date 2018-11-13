# coding=utf-8
# author:Biyoner
def judge_2(n):
    if n < 0:
        return "负数，错误"
    if not n&(n-1):
        return True
    else:
        return False

def change(n1,n2):
    n = n1^n2
    count = 0
    while n:
        count += 1
        n = n&(n-1)
    return count


if __name__ == "__main__":
    print judge_2(9)
    print change(10,13)