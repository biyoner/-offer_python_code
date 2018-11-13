import heapq


class DynamicArray(object):
    def __init__(self):
        self.heapmax =[]
        self.heapmin = []
        self.Max =  float('-inf')
        self.Min =  float('inf')

    def Insert(self, i):
        count = len(self.heapmax) + len(self.heapmin) + 1
        if count & 1:
            if i > self.Min:
                heapq.heappush(self.heapmax, -1 * heapq.heappushpop(self.heapmin, i))
                self.Min = self.heapmin[0]
            else:
                heapq.heappush(self.heapmax, -i)
            self.Max = self.heapmax[0]
        else:
            if i < -self.Max:
                heapq.heappush(self.heapmin, -1 * heapq.heappushpop(self.heapmax, -i))
                self.Max = self.heapmax[0]
            else:
                heapq.heappush(self.heapmin, i)
            self.Min = self.heapmin[0]
        # print self.heapmin,self.heapmax
        if count & 1:
            return -self.Max
        else:
            return (float(-self.Max) + float(self.Min)) /2


def Test(name,result,expectResult):
    if abs(result - expectResult)<0.0000001:
        print name + " is passed !"
    else:
        print name + " is failed !"

if __name__ == "__main__":
    numbers = DynamicArray()

    Test("Test2", numbers.Insert(5), 5)

    Test("Test3", numbers.Insert(2), 3.5)

    Test("Test4", numbers.Insert(3), 3)

    Test("Test5", numbers.Insert(4), 3.5)

    Test("Test6", numbers.Insert(1), 3)

    Test("Test7", numbers.Insert(6), 3.5)

    Test("Test8", numbers.Insert(7), 4)

    Test("Test9", numbers.Insert(0), 3.5)

    Test("Test10", numbers.Insert(8), 4)
