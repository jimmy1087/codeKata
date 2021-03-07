'''
a = [4,2,7,1,3]

i = 1, temp = a[1] = (2), j = 0
while j >= 0
    4 > 2 .. shift 4 to right .. [_,4,7,1,3] .. j = -1 = -1 .. 
insert item 2 at j + 1      [2,4,7,1,3]
i = 2  temp = a[2] = (7), j = 1
while j >= 0
    4 < 7
insert a[2] = 7 in j+1   [2,4,7,1,3]
i = 3  temp = a[3] = (1), j = 2
while j >= 0
    7 > 1 .. shift 7 to right .. [2,4,_,7,3] .. j = -1 = 1  .. 
    4 > 1 .. shift 4 to right .. [2,_,4,7,3] .. j = -1 = 0  ..
    2 > 1 .. shift 2 to right .. [_,2,4,7,3] .. j = -1 = -1 ..
insert item 1 at j + 1      [1,2,4,7,3]
i = 4  temp = a[4] = (3), j = 3
    7 > 3 .. shift 7 to right .. [1,2,4,_,7] .. j = -1 = 2 ..
    4 > 3 .. shift 4 to right .. [1,2,_,4,7] .. j = -1 = 1 ..
    2 < 3
insert a[4] = 3 in j+1   [1,2,3,4,7]

'''
def insertionSort(array):
    for i in range(1,len(array)):
        item = array[i]
        j = i-1
        while j >= 0:
            if array[j] > item:
                array[j+1] = array[j]
                j -= 1
            else:
                break
        
        array[j + 1] = item
    return array



a = [3,4,-6,2,1,4,6,-2,-3,0]

print('1st input', a[:])
print('1st output', insertionSort(a))

a = [5,4,3,2,1]

print('2nd input:', a[:])
print('2nd output', insertionSort(a))