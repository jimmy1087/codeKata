def anagram(s):
    if len(s) == 1:
        return s
    a = []
    subanagrams = anagram(s[1:])             # O(N!) asume anagram(s[1:]) will somehow solve the solution -1 char.
    for permutation in subanagrams:
        for i in range(len(permutation)+1):
            c = permutation[:]
            c = list(c)
            c.insert(i, s[0])
            a.append(''.join(c))
    return a

print(*anagram('abc'), sep='\n')

print(*anagram('abcde'), sep='\n')
print('Total combinations: ', len(anagram('abcde')))


