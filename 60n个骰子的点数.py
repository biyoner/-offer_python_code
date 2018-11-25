#codeing = utf-8
#author: Biyoner

g_maxValue = 6
def PrintProbability_Solution1(number):
    if number<=0:
        return

    maxSum = number*g_maxValue
    i = number
    pProbability = []
    while i<=maxSum:
        pProbability.append(0)
        i += 1
    pProbability = Probability(number,pProbability)
    for i in range(len(pProbability)):
        ratio = pProbability[i] *1.0 / float(pow(g_maxValue,number))
        print "%d:%e" %(i+number,ratio)

def Probability(number, pProbability):

    return ProbabilityCore(number, number, 0, pProbability)

def ProbabilityCore(all,number,sum,pProbability):

    if number == 0:
        pProbability[sum-all] += 1
        return pProbability

    for i in range(1,g_maxValue+1):
        pProbability = ProbabilityCore(all,number-1,sum+i,pProbability)

    return pProbability

def PrintProbability_Solution2(number):
    if number<=0:
        return
    pProbability = [[],[]]

    i = 0
    while i <= number*g_maxValue:
            pProbability[0].append(0)
            pProbability[1].append(0)
            i += 1

    #Initialization
    for i in range(1,g_maxValue+1):
        pProbability[0][i] += 1

    # Begin Iteration
    flag = 1
    for k in range(2,number+1):
        for i in range(k):
            pProbability[flag][i] = 0

        for i in range(k,g_maxValue*k+1):
            pProbability[flag][i] = 0
            j = 1
            while j<=g_maxValue and i-j>=0:
                pProbability[flag][i] += pProbability[1-flag][i-j]
                j += 1

        flag = 1 - flag

    for i in range(len(pProbability[1-flag])):
        if pProbability[1-flag][i] != 0:
            ratio = pProbability[1-flag][i] *1.0 / float(pow(g_maxValue,number))
            print "%d: %.10f" %(i+number,ratio)

def Test(n):

    print("Test for %d begins:", n)

    print("Test for solution1")
    PrintProbability_Solution1(n)

    print("Test for solution2")
    PrintProbability_Solution2(n)



if __name__ ==  "__main__":
    Test(1)
    Test(2)
    Test(3)
    Test(4)
    Test(11)
    Test(0)