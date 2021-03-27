def squaredArray(array):

    positiveStartsAt = -1
    for idx, item in enumerate(array):

        # 2 Identify where positive numbers start
        if item >= 0 and positiveStartsAt == -1:
            positiveStartsAt = idx
            break
    
    #3. Set left and right pointer
    leftIdx  = positiveStartsAt - 1
    rightIdx = positiveStartsAt

    #4. o(n) loop on both direction using a merge philosophy
    result = []
    while len(result) != len(array):

        if leftIdx < 0:
            result += [array[rightIdx]**2]
            rightIdx += 1
            continue
        elif rightIdx > len(array):
            result += [array[leftIdx]**2]
            leftIdx -= 1
            continue
    
        if abs(array[leftIdx]) <= array[rightIdx]:
            result += [array[leftIdx]**2]
            leftIdx -= 1
        else:
            result += [array[rightIdx]**2]
            rightIdx += 1
    
    return result

    


a = [-7, -3, -1, 4, 8, 12]

print(squaredArray(a))

'''
1. Store { Abs(idx): squared }
m = { 7: 49, 3: 9, 1: 1, 4: 16, 8:12, 12:144 }

2. Identify where positives start
positiveStartAtIdx = 3

3. Set left and right pointer
leftIdx = 2
rightIdx = 3

4. o(n) loop on both direction using a merge philosophy
leftV vs rightV   <     move pointer    array
1 or 4,           1,    leftIdx = 1     a = [1]
3 or 4,           3,    leftIdx = 0     a = [1,9]
7 or 4,           4,    rightIdx = 4    a = [1,9,16]
7 or 8,           7,    leftIdx = -1    a = [1,9,16,49]
8                 8,    rightIdx = 5    a = [1,9,16,49,64]
12               12,    rightIdx = 6    a = [1,9,16,49,64,144]

output: [1,9,16,49,64,144]

'''