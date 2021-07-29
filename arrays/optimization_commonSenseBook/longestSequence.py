# write a function that accepts an array of unsorted integers 
# and returns the length of the longest consecutive sequence among them. 

def longestSequenceLen(array):
    
    t = {}
    for n in array:
        t[n] = True

    longest = 0
    for n in array:
        # Traverse only when number is at the bottom of a sequence
        if n - 1 not in t:
            sequence = n
            tempLen = 1
            while sequence + 1 in t:
                sequence = sequence + 1
                tempLen += 1
            longest = max(tempLen, longest)

    print(longest)

array = [10, 5, 12, 3, 55, 30, 4, 11, 2]

longestSequenceLen(array)

array = [19, 13, 15, 12, 18, 14, 17, 11]

longestSequenceLen(array)