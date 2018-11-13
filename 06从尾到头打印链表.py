# coding=utf-8
# author:Biyoner
class Node(object):
    def __init__(self,data,pnext =  None):
        self.data = data
        self._next = None

    def __repr__(self):
        return str(self.data)

class chaintable(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self,dataOrNode):
        item = None
        if isinstance(dataOrNode,Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if not self.head:
            self.head = item
        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.length += 1

    def isEmpty(self):
        return (self.length==0)

    def __repr__(self):
        if self.isEmpty():
            print "The table is empty!"

        node = self.head
        nlist = ''
        while node:
            nlist += str(node.data)+" "
            node = node._next
        return nlist
    def reverse_chain(self):
        if self.isEmpty():
            print "The table is empty!"
        node = self.head
        nlist = []
        while node:
            nlist.append(str(node.data))
            node = node._next
        # nlist.reverse()
        nlist = nlist[::-1]
        return nlist

if __name__ == "__main__":
    chain1  = chaintable()
    for i in range(1,6):
        chain1.append(i)
    new1 = chain1.reverse_chain()
    print new1

    chain2 = chaintable()
    chain2.append(1)
    new2 = chain2.reverse_chain()
    print new2

    chain3 = chaintable()
    new3 = chain3.reverse_chain()
    print new3