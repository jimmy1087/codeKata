'''
 Selection Sort is actually more efficient than bubble sort in terms of Steps. Eventhough it is classified as O(N^2)
 Number of steps to order a descending array of 5 elements would be
 16 steps:    

    i:0  j: 1..4   1 step of i + 4 steps j  = 5
    i:1  j: 2..4   1 step of i + 3 steps j  = 4
    i:2  j: 3..4   1 step of i + 2 steps j  = 3
    i:3  j: 4..4   1 step of i + 1 steps j  = 2

    swaps [5,4,3,2,1]   1 for 5  .. [1,4,3,2,5]   1 step
    swaps [1,4,3,2,5]   4 for 2  .. [1,2,3,4,5]   1 step

    total steps = 16
'''

def selectionSort(a):
    step = 0
    for i in range(0, len(a)-1):
        print('i',i)
        step += 1
        minValueIdx = i
        for j in range(i+1, len(a)):
            print('j',j)
            step += 1
            if a[j] < a[minValueIdx]:
                minValueIdx = j
        
        if a[i] != a[minValueIdx]:
            print('Switch', a[i], a[minValueIdx])
            step += 1
            tmp = a[minValueIdx]
            a[minValueIdx] = a[i]
            a[i] = tmp

    print('Total Steps:', step)
    return a

#a = [3,4,-6,2,1,4,6,-2,-3,0]

#print('1st input', a[:])
#print('1st output', selectionSort(a))

a = [5,4,3,2,1]

print('2nd input:', a[:])
print('2nd output', selectionSort(a))
