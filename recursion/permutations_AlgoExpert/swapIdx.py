def getPermutations(array):
    array = list(array)
    permutations = []
    getPermutationsHelper(0, array, permutations)
    return permutations

# O(n!n) T || O(n!n) S -> For every new array
# This time we do not get n*n because we are not creating a new array, we are swaping elements in place and this is a O(1) operation
# See written notes in Black Leather Notebook
def getPermutationsHelper(idx, array, permutations):
    
    if idx == len(array) - 1:
        permutations.append(array[:])
        return

    for j in range(idx, len(array)):

        swap(idx, j, array)
        getPermutationsHelper(idx + 1, array, permutations)
        swap(idx, j, array)

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

a = 'ABC'
print(*getPermutations(a),sep='\n')