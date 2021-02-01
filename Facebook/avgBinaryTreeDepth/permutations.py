


def permutations(array):
    r = []
    for i in range(len(array)):
        permutationArray = array[:]
        firstElement = permutationArray.pop(i)
        for j in range(len(permutationArray)):
            colArray = permutationArray[:]
            permutation = [firstElement]
            permutation.append(colArray.pop(j))
            while colArray:
                permutation.append(colArray.pop())
            r.append(permutation)
    print(r)

t = [5,7,9]

permutations(t)