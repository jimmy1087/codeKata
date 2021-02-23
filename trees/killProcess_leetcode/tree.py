class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

# o(n) Time | o(n) Space
def killProcess(pid, ppid, kill):

    # o(n) Time | o(n) Space
    m = {}
    for p in pid:
        m[p] = Node(p)

    # o(n) Time
    for i, p in enumerate(ppid):
        if p == 0:
            continue
        pp = m[p]
        pp.children.append( m[ pid[i] ] )

    toKill = []
    dfs(m, kill, toKill)

    return toKill

# o(n) Time | # o(n) Space
def dfs(m, kill, toKill):
    toKill.append(kill)
    for child in m[kill].children:
        dfs(m, child.value, toKill)

'''
pid:  [1,3,10,5,2,8]
ppid: [3,0, 5,3,5,10]
kill: 5

1. Create a dictionary of nodes with all the PID values
    m = {
        1: Node(1),
        3: Node(3),
        10: Node(10),
        5: Node(5),
        2: Node(2),
        8: Node(8)
    }
2. For each item in PPID, fill the children list with the Node from the PID array
    N(3).children  = [ N(1) ]
    N(0) skip
    N(5).children  = [ N(10) ]
    N(3).children  = [ N(1), N(5) ] 
    N(5).children  = [ N(10), N(2) ] 
    N(10).children = [ N(8) ]

2.1 Which will create a tree conected
 
        N(3)
         / \
      N(1) N(5)
           / \
       N(10) N(2)
        /
    N(8)

3. From Kill Node, traverse children nodes in DFS and add node to response list

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
    return toKill[5, 10, 8, 2]

'''

pid  =  [1,3,10,5,2,8]
ppid =  [3,0,5,3,5,10]
kill =  5

print(killProcess(pid, ppid, kill))