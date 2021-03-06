def numDecodings(s):
    memo = {}
    n = numberOfWays(s, memo)
    print(memo)
    return n

def numberOfWays(s, m):
    if m.get(s) is not None:
        print('memo['+s+']', m[s])
        return m[s]

    if len(s) == 0:
        print('len == 0: +1 ', s)
        return 1
    
    if s[0] == '0':
        return 0
    
    if len(s) == 1:
        print('Valid: +1 ', s)
        return 1

    print(s[0:1])
    ans = numberOfWays(s[1:], m)
    print(s[0:2])

    if int(s[0:2]) <= 26:
        ans += numberOfWays(s[2:], m)
    else:
        print('Rejected',s[0:2])
    
    print('Store in memo['+s+']', ans)
    m[s] = ans
    return ans

s = '12'
print(numDecodings(s), s)