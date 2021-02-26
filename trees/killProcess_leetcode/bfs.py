'''
pid:  [1,3,10,5,2,8]
ppid: [3,0, 5,3,5,10]

m = { 3: [1,5], 0: [3], 5: [10,2], 10:[8] }
queue = [5]
5 = queue.pop()
toKill[5]
queue[10, 2]
10 = queue.pop()
toKill[5, 10]
queue[2, 8]
2 = queue.pop()
toKill[5, 10, 2]
8 = queue.pop()
toKill[5, 10, 2, 8]
return

'''

def killProcess(pid, ppid, kill):

    m = {}
    for i, p in enumerate(ppid):
        if m.get(p) is None:
            m[p] = [pid[i]]
        else:
            m[p].append(pid[i])
    
    toKill = []
    bfs(m, kill, toKill)

    return toKill

def bfs(m, kill, toKill):
    queue = [kill]
    while queue:
        p = queue.pop(0)
        toKill.append(p)
        if m.get(p) is not None:
            for child in m[p]:
                queue.append(child)
    
#Tests

pid  =  [1,3,10,5,2,8]
ppid =  [3,0,5,3,5,10]
kill =  5

print(killProcess(pid, ppid, kill))

pid  =  [1,2,3,4,5]
ppid =  [0,1,1,1,1]
kill =  1

print(killProcess(pid, ppid, kill))

pid  =  [1,3,10,5,2,8,9,7]
ppid =  [3,0,5,3,5,10,8,2]
kill =  5

print(killProcess(pid, ppid, kill))