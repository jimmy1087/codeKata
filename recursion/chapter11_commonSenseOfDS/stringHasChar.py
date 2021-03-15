def stringHasChar(s, c, i=0):
    if len(s) == 0:
        return -1
    if s[0] == c:
        return i
    return stringHasChar(s[1:], c, i+1)


s = "abcdefghijklmnopqrstuvwxyz"
c = 'x'

print(stringHasChar(s,c))