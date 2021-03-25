'''
o(n^2) 5 * 5 = 25 steps to sort an array of 5 elements that were in desc order.
'''

def bubbleSort(array):
    steps = 0
    outerLoop = 1
    sorted = False
    sortedElements = 0
    while not sorted:
        steps += 1
        print('[[loop]]', outerLoop)
        outerLoop += 1
        sorted = True
        for i in range(len(array)-sortedElements-1):
            print('i', i)
            steps += 1
            if array[i] > array[i+1]:
                print('Swap', array[i], array[i+1])
                steps += 1
                swap(i, array)
                sorted = False
        sortedElements += 1
    print('Total steps: ', steps)
    return array

def swap(i, array):
    array[i], array[i+1] = array[i+1], array[i]
        
#a = [3,4,-6,2,1,4,6,-2,-3,0]
#print(bubbleSort(a))

a = [5,4,3,2,1]
print(bubbleSort(a))