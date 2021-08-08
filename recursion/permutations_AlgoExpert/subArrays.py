def getPermutations(array):
    permutations = []
    getPermutationsHelper(array, '', permutations)
    return permutations

# O(N! * N^2) T || O(n!n) S -> For every new array
# N! * N -> It is a Tree of permutations, each branch will contain a possible permutation. 
#           At the leaf level you get each possible Permutation n! 
#           but the lenght of each branch is of length "n". Thus this is o(n!*n)
# The other n comes from the Time complexity of creating new arrays. O(n + n) --> O(n)
#
# Result we get O(!N * n) * O(N) -->   O(N! * N^2)
# See written notes in Black Leather Notebook or video explanation of Permutation problem in AlgoExpert
def getPermutationsHelper(array, perm, perms):
    
    if len(array) == 0:
        perms.append(perm)
        return
    
    for idx in range(len(array)):
        newArray = array[:idx] + array[idx + 1:] # --> O(n) creation of a new array
        newPerm = perm + array[idx]              # --> O(n) creation of a new array
        getPermutationsHelper(newArray, newPerm, perms)
    
a = "ABC"
print(*getPermutations(a), sep='\n')