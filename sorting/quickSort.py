
class SortArray:

    def __init__(self, array):
        self.array = array

    def quickSort(self, leftIdx, rightIdx):
        
        if rightIdx - leftIdx <= 0:
            return
        
        pivotIdx = self.partition(leftIdx, rightIdx)

        self.quickSort(leftIdx, pivotIdx - 1)
        self.quickSort(pivotIdx, rightIdx)

    '''
    1. The left pointer continuously moves one cell to the right until it reaches a value that is greater than or equal to the pivot, and then stops.
    2. Then, the right pointer continuously moves one cell to the left until it reaches a value that is less than or equal to the pivot, and then stops. The right pointer will also stop if it reaches the beginning of the array.
    3. Once the right pointer has stopped, we reach a crossroads. If the left pointer has reached (or gone beyond) the right pointer, we move on to Step 4. Otherwise, we swap the values that the left and right pointers are pointing to, and then go back to repeat Steps 1, 2, and 3 again.
    4. Finally, we swap the pivot with the value that the left pointer is currently pointing to.
    '''
    def partition(self, leftIdx, rightIdx):
        
        pivotIdx = rightIdx
        pivot = self.array[pivotIdx]
        
        while True:
            
            while self.array[leftIdx] < pivot:
                leftIdx += 1

            while self.array[rightIdx] > pivot:
                rightIdx -= 1

            if leftIdx >= rightIdx:
                break
            
            self.array[leftIdx], self.array[rightIdx] = self.array[rightIdx], self.array[leftIdx]
            leftIdx += 1

        self.array[leftIdx], self.array[pivotIdx] = self.array[pivotIdx], self.array[leftIdx]
        
        return leftIdx

    def getSortedArray(self):
        return self.array


a = [0,5,2,1,6,3]
c = SortArray(a)
c.quickSort(0,len(a)-1)
print(c.getSortedArray())


