# coding=utf-8
# author:Biyoner
class Queue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self,item=None):
        if item:
            self.stack1.append(item)


    def deleteHead(self):
        if len(self.stack2) == 0 and len(self.stack1)==0:
            return "Error"
        if len(self.stack2)!= 0:
            pass
        else:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

if __name__ == "__main__":
    q = Queue()
    q.appendTail("a")
    q.appendTail("b")
    q.appendTail("c")
    print(q.deleteHead())
    print(q.deleteHead())
    q.appendTail("d")
    print(q.deleteHead())