#coding = utf-8
#author: Biyoner

class QueueWithMax(object):
    def __init__(self):
        self.maximuns = []

        self.data = []
        self.currentIndex = 0
    def push_back(self,val):

        if len(self.maximuns)>0 and self.maximuns[-1]["number"]<val:
            self.maximuns.pop()
        InternalData = {"Index":self.currentIndex,"number":val}
        self.data.append(InternalData)
        self.maximuns.append(InternalData)

        self.currentIndex += 1

    def pop_front(self):
        if len(self.maximuns) == 0:
            return "queue is empty"

        if self.data[0]["Index"] == self.maximuns[0]["Index"]:
            self.maximuns = self.maximuns[1:]

        self.data = self.data[1:]

    def Max(self):
        if len(self.maximuns) == 0:
            return "queue is empty"

        return self.maximuns[0]["number"]

def Test(name,q,expectValue):

    if q.Max() == expectValue:
        print name + " is passed !"
    else:
        print name + " is failed !"

if __name__ == "__main__":
    queue = QueueWithMax()
    # // {2}
    queue.push_back(2)
    Test("Test1", queue, 2)

    # // {2, 3}
    queue.push_back(3)
    Test("Test2", queue, 3)

    # // {2, 3, 4}
    queue.push_back(4)
    Test("Test3", queue, 4)

    # // {2, 3, 4, 2}
    queue.push_back(2)
    Test("Test4", queue, 4)

    # // {3, 4, 2}
    queue.pop_front()
    Test("Test5", queue, 4)

    # // {4, 2}
    queue.pop_front()
    Test("Test6", queue, 4)

    # // {2}
    queue.pop_front()
    Test("Test7", queue, 2)

    # // {2, 6}
    queue.push_back(6)
    Test("Test8", queue, 6)

    # // {2, 6, 2}
    queue.push_back(2)
    Test("Test9", queue, 6)

    # // {2, 6, 2, 5}
    queue.push_back(5)
    Test("Test9", queue, 6)

    # // {6, 2, 5}
    queue.pop_front()
    Test("Test10", queue, 6)

    # // {2, 5}
    queue.pop_front()
    Test("Test11", queue, 5)

    # // {5}
    queue.pop_front()
    Test("Test12", queue, 5)

    # // {5, 1}
    queue.push_back(1)
    Test("Test13", queue, 5)