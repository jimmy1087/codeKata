import random

class MinHeap:

    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        idx = len(array) - 1
        parentIdx = (idx - 1) // 2
        while parentIdx >= 0:
            self.siftDown(parentIdx, array)
            parentIdx -= 1
        print(array)
        return array

    def siftDown(self, nodeIdx, array):
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

    def siftUp(self, nodeIdx, array):
        parentIdx = (nodeIdx - 1) // 2
        while nodeIdx > 0 and array[nodeIdx] < array[parentIdx]:
            self.swap(nodeIdx, parentIdx, array)
            nodeIdx = parentIdx
            parentIdx = (nodeIdx - 1) // 2

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap)
        print(self.heap)

    def remove(self):
        self.swap(0, len(self.heap)-1, self.heap)
        self.siftDown(0, self.heap)
        return self.heap.pop()

    def peek(self):
        return self.heap[0]

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]

a = [random.randrange(10) for _ in range(24)]
print('unorder', a)
minHeap = MinHeap(a)
print(minHeap.peek())
print(minHeap.remove())
print(minHeap.peek())
print(minHeap.insert(45))
print(minHeap.insert(-10))
print(minHeap.peek())