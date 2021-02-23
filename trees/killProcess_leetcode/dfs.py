def killProcess(pid, ppid, kill):
    idx = pid.index(kill)
    if ppid[idx] == 0:
        return pid
    toKill = []
    dfs(pid, ppid, kill, toKill)
    return toKill

# o(n^2) time | o(1)
def dfs(pid, ppid, kill, toKill):
    toKill.append(kill)
    for i, p in enumerate(ppid):
        if p == kill:
            dfs(pid, ppid, pid[i], toKill)

### Tests
pid  =  [1,2,3,4,5]
ppid =  [0,1,1,1,1]
kill =  1

print(killProcess(pid, ppid, kill))

pid  =  [1,3,10,5,2,8,9,7]
ppid =  [3,0,5,3,5,10,8,2]
kill =  5
print(killProcess(pid, ppid, kill))
'''
        3
       / \
      1   5
         / \
       10   2
       /     \
      8       7
     /
    9

pid  =  [1,3,10,5,2, 8,9,7]
ppid =  [3,0, 5,3,5,10,8,2]
kill = 5

dfs(5)
    toKill: [5]
    dfs(10)
        toKill: [5,10]
        dfs(8)
            toKill: [5,10,8]
            dfs(9)
                toKill: [5,10,8,9]
                --
            --
        --
    dfs(2)
        toKill: [5,10,8,9,2]
        --
    --
toKill: [5,10,8,9,2]
'''