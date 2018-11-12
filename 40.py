#coding= utf-8
#author:Biyoner
import RBTree

def GetLeastNumbers(l,k):
    l = Partition(0,len(l)-1,l,k-1)
    return l[:k]
def Partition(begin,end,l,index):
    i = begin
    j = end
    base = l[begin]
    while i<j:
        while l[j]>=base and j>i:
            j -= 1
        l = swap(i,j,l)
        while l[i]<=base and j>i:
            i += 1
        l = swap(i,j,l)
    if i < index:
        return Partition(i+1,end,l,index)
    elif i>index:
        return Partition(begin,i-1,l,index)
    else:
        return l
def swap(i,j,l):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp
    return l


#思路： 当容器内数据需要频繁查找及替换最大值时，
# 二叉树是一个合适的选择，用堆或红黑树均能实现
def GetLeastNumbers2(l,k):
    count = 0
    tree = RBTree.RBTree()

    for i in l:
        if count <k:
            tree.add_node(RBTree.RBNode(i))
            count += 1
        else:
            maxVal = tree.get_Max_node().data
            if i < maxVal:
                tree.delete_node(maxVal)
                tree.add_node(RBTree.RBNode(i))
    return preOrder(tree.root)

def preOrder(root):
    if not root:
        return []
    left = preOrder(root.left)
    right = preOrder(root.right)

    return [root.data]+left+right
def checklist(l,k):
    flag = False
    if len(l) <= 0 or k>len(l) or k<=0:
        flag = True
    return flag

def Test(name, numbers, k, expectValue):
    if checklist(numbers,k):
        result = None
    else:
        result = GetLeastNumbers2(numbers, k)
        result = list(set(result))
        result.sort()
    if result == expectValue:
        print name + " is passed!"
    else:
        print name + " is failed!"

if __name__ == "__main__":
    Test("Test1",[4, 5, 1, 6, 2, 7, 3, 8],4,[1, 2, 3, 4])
    Test("Test2", [4, 5, 1, 6, 2, 7, 3, 8], 8, [1, 2, 3, 4, 5, 6, 7, 8])
    Test("Test3", [4, 5, 1, 6, 2, 7, 3, 8], 10, None)
    Test("Test4", [4, 5, 1, 6, 2, 7, 3, 8], 1, [1])
    Test("Test5", [4, 5, 1, 6, 2, 7, 3, 8], 0, None)
    # Test("Test6", [4, 5, 1, 6, 2, 7, 2, 8],3,[1,2])
    Test("Test7", [], 0, None)
