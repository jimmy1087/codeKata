'''
                        0 -> X
                    1
                        06 -> X

                    1   06  -> X
                1
                    10  6  -> OK            [1, 1, 10, 6] valid

            1       0 -> X
                11
                    06 -> X

    11106           0 -> X
                1
                    06 -> X
            11  
                10  6  -> OK                [11, 10, 6] valid
'''


def numDecodings(s):
    m = {}
    n = numberOfWays(s, m)
    print(m)
    return n

def numberOfWays(s, m):
    
    if s[0] == '0':
            return 0
    if m.get(s) is not None:
        return m[s]
    if len(s) == 1:
        if isSingleCharValid(s[0]):
            m[s[0]] = 1
            return 1
        else:
            return 0
    elif len(s) == 2:
        if s[0] == '0':
            return 0
        elif isTwoCharsValid(s[0], s[1]):
            return numberOfWays(s[1:], m) + 1
        else:
            return numberOfWays(s[1:], m)

    ans = numberOfWays(s[1:], m)
    if isTwoCharsValid(s[0], s[1]):
        ans += numberOfWays(s[2:], m) 
    m[s] = ans
    return ans

def isSingleCharValid(c):
    return c != '0'

def isTwoCharsValid(c1, c2):
    n = int(c1) * 10 + int(c2)
    if n < 10 or n > 26:
        return False
    return True

s = '21253'
print(numDecodings(s), s)