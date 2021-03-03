def bubbleSort(array):
    sorted = False
    sortedElements = 0
    while not sorted:
        sorted = True
        for i in range(len(array)-sortedElements-1):
            if array[i] > array[i+1]:
                swap(i, array)
                sorted = False
        sortedElements += 1
    return array

def swap(i, array):
    array[i], array[i+1] = array[i+1], array[i]
        
a = [3,4,-6,2,1,4,6,-2,-3,0]

print(bubbleSort(a))