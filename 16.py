# coding=utf-8
# author:Biyoner
g_InvalidInput = False
def Power(base,exponet):
    g_InvalidInput = False
    val = 1.0
    base = float(base)
    if base == 0 and exponet<0:
        g_InvalidInput = True
        return 0.0
    val = PowersubRecur(base,abs(exponet))
    if exponet <0:
        val = 1.0/val
    return val

def PowersubLoop(base,exponet):
    val = 1.0
    for i in range(abs(exponet)):
            val = val*base
    return val

def PowersubRecur(base,exponet):
    if exponet == 0:
        return 1
    if exponet == 1:
        return base
    result = PowersubRecur(base,exponet>>1)
    result *= result
    if (exponet&0x1 == 1):
        result *= base
    return result

def Test(inputs):
    base = inputs[0]
    exponet = inputs[1]
    value = inputs[2]
    if (Power(base,exponet) -value)<0.0000001 and (Power(base,exponet) -value)>-0.0000001 and not g_InvalidInput:
        return "Test passed !"
    else:
        return "Test failed !"




if __name__ == "__main__":
    tests = [[2, 3, 8],[-2, 3, -8],[2, -3, 0.125],[2, 0, 1],[0, 0, 1],[0, 4, 0],[0, -4, 0]]
    for item in tests:
        print Test(item)
