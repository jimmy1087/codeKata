def mergeIntervals(a):

    sortedArray = sorted(a, key=lambda x: x[0])
    mergeArray = []

    currentItem = sortedArray[0]
    mergeArray.append(currentItem)

    for nextItem in sortedArray:

        _, currentEnd = currentItem
        nextStart, nextEnd = nextItem

        if currentEnd >= nextStart:
            currentItem[1] = max(currentEnd, nextEnd)
        else:
            currentItem = nextItem
            mergeArray.append(nextItem)
    
    return mergeArray


a = [[4,7],[6,8],[9,10],[3,5],[1,2]]

'''
1. sortArray:   [[1,2],[3,5],[4,7],[6,8],[9,10]]
2. 

1st loop
    currentItem: [1,2]    mergeArray: [1,2]
    nextItem: [1,2]
    currentEnd: 2     nextStart: 1   nextEnd: 2      --> It doesn't matter if the first iteration it process the same currentItem
    if currentEnd(2) >= nextStart(1) --> True
        currentItem[1] = max(2,2)  --> 1st iteration overrides with same value
2nd loop
    currentItem: [1,2]    mergeArray: [1,2]
    nextItem: [3,5]
    currentEnd: 2    nextStart: 3   nextEnd: 5
    if currentEnd(2) >= nextStart(3) --> False
    else:  
        currentItem = [3,5]
        mergeArray: [1,2][3,5]
3rd loop
    currentItem: [3,5]   mergeArray: [1,2][3,5]
    nextItem: [4,7]
    currentEnd: 5   nextStart: 4  nextEnd: 7
    if currentEnd(5) >= nextStart(4)  --> True
        currentItem[1] = max(5,7)  --> 7
4rd loop
    currentItem: [3,7]   mergeArray: [1,2][3,7] .... etc

expected output:   [[1, 2], [3, 8], [9, 10]]
'''

print(mergeIntervals(a))