# coding=utf-8
# author:Biyoner
import numpy as np
def fib_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1)+fib_recur(n-2)

def fib_loop(n):
    first = 0
    second = 1
    new = None
    if n == 0 or n == 1:
        return n
    for i in range(n-1):
        new = first + second
        first = second
        second = new
    return new


def multi(r,n):
    if n <= 0:
        return 0
    if n == 1:
        return r
    if n%2 ==0:
        return multi(r,n/2)*multi(r,n/2)
    if n%2 == 1:
        return multi(r,(n-1)/2) * multi(r,(n-1)/2)*r

def fib_matrix(n):
    if n == 0 or n == 1:
        return n
    else:
        r = np.mat([[1,1],[1,0]],dtype=np.float64)
        matrix = multi(r,n-1)
        return matrix[0,1]+matrix[1,1]


if __name__ == "__main__":
    n = 2
    print fib_recur(n)
    print fib_loop(n)
    print fib_matrix(n)
