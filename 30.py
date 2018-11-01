#coding= utf-8
#author:Biyoner

class Stack(object):
    def __init__(self):
        self.data = []
        self.min = []

    def pop(self):
        ld = len(self.data)
        lm = len(self.min)
        if ld > 0 and lm>0:
            self.data = self.data[:-1]
            self.min = self.min[:-1]



    def push(self,data):
        self.data.append(data)
        l = len(self.min)
        if l == 0:
            self.min.append(data)
        else:
            if data < self.min[-1]:
                self.min.append(data)
            else:
                self.min.append(self.min[-1])

    def Min(self):
        if len(self.min)>0:
            return self.min[-1]
        else:
            return None
def Test(name, stack, result):
    if stack.Min() == result:
        print name + " " + "is passed !"
    else:
        print name + " " + "is failed !"
if __name__ == "__main__":
    stack = Stack()
    stack.push(3)
    Test("Test1", stack, 3)

    stack.push(4)
    Test("Test2", stack, 3)

    stack.push(2)
    Test("Test3", stack, 2)

    stack.push(3)
    Test("Test4", stack, 2)

    stack.pop()
    Test("Test5", stack, 2)

    stack.pop()
    Test("Test6", stack, 3)

    stack.pop()
    Test("Test7", stack, 3)

    stack.push(0)
    Test("Test8", stack, 0)


