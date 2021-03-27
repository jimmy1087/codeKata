# o(n) time || o(n) space due to copy of array
def reverseStr(string):
    r = []
    idx = len(string)-1
    while idx >= 0:
        r.append(string[idx])
        idx -= 1
    return ''.join(r)

print(reverseStr('ABCDE'))