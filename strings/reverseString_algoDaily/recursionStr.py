
# O(n) time || o(n) space due to call stack
def reverseStr(string):
    if len(string) == 1:
        return string
    return reverseStr(string[1:]) + string[0]

print(reverseStr('ABCDE'))