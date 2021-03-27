def squaredSortedArray(array):

    result = [0 for _ in array]

    leftIdx = 0
    rightIdx = len(array)-1

    for i in reversed(range(len(array))):

        if abs(array[leftIdx]) >= abs(array[rightIdx]):
            result[i] = array[leftIdx]**2
            leftIdx += 1
        else:
            result[i] = array[rightIdx]**2
            rightIdx -=1

    return result


a = [-7, -3, -1, 4, 8, 12]

print(squaredSortedArray(a))