# coding=utf-8
# author:Biyoner
from collections import deque
class Stack(object):
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    def add(self,val):
        if len(self.q1)!=0 and len(self.q2)==0:
            self.q1.append(val)
        elif len(self.q1)==0 and len(self.q2)!=0:
            self.q2.append(val)
        elif len(self.q1)==0 and len(self.q2)==0:
            self.q1.append(val)
        else:
            return "Inter Error"

    def delete(self):
        if len(self.q1)!=0 and len(self.q2)==0:
            for i in range(len(self.q1)-1):
                self.q2.append(self.q1.popleft())
            return self.q1.popleft()
        elif len(self.q1)==0 and len(self.q2)!=0:
            for i in range(len(self.q2) - 1):
                self.q1.append(self.q2.popleft())
            return self.q2.popleft()
        elif len(self.q1) == 0 and len(self.q2) == 0:
            return "The stack is None!"
        else:
            return "Inter Error"


if __name__ == "__main__":
    s = Stack()
    s.add('a')
    s.add('b')
    s.add('c')
    print s.delete()
    print s.delete()
    s.add('d')
    print s.delete()
