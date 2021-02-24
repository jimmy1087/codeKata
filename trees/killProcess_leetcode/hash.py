def killProcess(pid, ppid, kill):

    # o(n) time | o(n) space
    m = {}
    for i, p in enumerate(ppid):
        if m.get(p) is None:
            m[p] = [ pid[i] ]
        else:
            m[p].append( pid[i] )
    
    toKill = []
    dfs(m, kill, toKill)

    return toKill

# o(n) time | o(n) space
def dfs(m, kill, toKill):
    toKill.append(kill)
    if m.get(kill) is None:
        return
    for v in m[kill]:
        dfs(m, v, toKill)


'''
pid  =  [1,3,10,5,2,8]
ppid =  [3,0, 5,3,5,10]
kill =  5

m: { 3: [1, 5], 0: [3], 5: [10, 2], 10: [8] }

dfs(5)
    toKill[5]
    dfs(10)
        toKill[5, 10]
        dfs(8)
            toKill[5, 10, 8]
            --
        --
    dfs(2)
        toKill[5, 10, 8, 2]
    --
--
toKill[5, 10, 8, 2]

'''

pid  =  [1,3,10,5,2,8]
ppid =  [3,0,5,3,5,10]
kill =  5

print(killProcess(pid, ppid, kill))