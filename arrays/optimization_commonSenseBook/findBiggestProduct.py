def findBiggestProduct(array):

    maxFirstPositive = 0
    maxSecPositive = 0
    maxFirstNegative = 0
    maxSecNegative = 0

    for n in array:

        if n > 0:
            if n > maxFirstPositive:
                maxSecPositive = maxFirstPositive
                maxFirstPositive = n
            elif n > maxSecPositive:
                maxSecNegative = n
        elif n < 0:
            if n < maxFirstNegative:
                maxSecNegative = maxFirstNegative
                maxFirstNegative = n
            elif n < maxSecNegative:
                maxSecNegative = n
        
    return max(maxFirstPositive * maxSecNegative, maxFirstNegative * maxSecNegative)


a = [5, -10, 9, 4, -6]
print(findBiggestProduct(a))
a = [-6, -5, -1, 2, 3, 9] #-> Greatest product: 30 (-6 * -5)
print(findBiggestProduct(a))