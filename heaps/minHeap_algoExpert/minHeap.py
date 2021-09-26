import random

class MinHeap:

    c = 0
    sd = 0

    def __init__(self, array):
        self.heap = self.buildHeap(array)

    # O(n) time || O(1) space
    def buildHeap(self, array):
        idx = len(array) - 1
        parentIdx = (idx - 1) // 2
        while parentIdx >= 0:
            self.siftDown(parentIdx, array)
            parentIdx -= 1
        #print('Times: ' + str(self.c))
        return array

    # O(logN) time || O(1) space
    def siftDown(self, nodeIdx, array):
        self.sd = 0
        while nodeIdx < len(array)-1:
            leftIdx = 2 * nodeIdx + 1
            rightIdx = 2 * nodeIdx + 2
            # If nodeIdx is a leaf then exit
            if leftIdx >= len(array):
                break
            # Get smaller node from childs
            swapIdx = leftIdx if rightIdx > len(array)-1 or array[leftIdx] < array[rightIdx] else rightIdx
            if array[swapIdx] > array[nodeIdx]:
                break
            self.swap(swapIdx, nodeIdx, array)
            nodeIdx = swapIdx
            self.c += 1
            self.sd += 1

    # O(logN) time || O(1) space
    def siftUp(self, nodeIdx, array):
        parentIdx = (nodeIdx - 1) // 2
        while nodeIdx > 0 and array[nodeIdx] < array[parentIdx]:
            self.swap(nodeIdx, parentIdx, array)
            nodeIdx = parentIdx
            parentIdx = (nodeIdx - 1) // 2

    # O(logN) time || O(1) space
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap)
        print(self.heap)

    # O(logN) time || O(1) space
    def remove(self):
        self.swap(0, len(self.heap)-1, self.heap)
        self.siftDown(0, self.heap)
        return self.heap.pop()

    def peek(self):
        return self.heap[0]

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]
    
    def getNCounter(self):
        return self.c

    def getSDCounter(self):
        return self.sd

timesN = []
timesSD = []
for _ in range(100):
    a = [random.randrange(1000) for _ in range(1000000)]
    minHeap = MinHeap(a)
    c = minHeap.getNCounter()
    timesN.append(c)
    minHeap.remove()
    d = minHeap.getSDCounter()
    timesSD.append(d)
    
print('TimeToBuild', sum(timesN)/len(timesN))
print('TimeToSiftDown', sum(timesSD)/len(timesSD))
'''
print(minHeap.peek())
print(minHeap.remove())
print(minHeap.peek())
print(minHeap.insert(45))
print(minHeap.insert(-10))
print(minHeap.peek())
'''