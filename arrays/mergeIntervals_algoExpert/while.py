def mergeIntervals(a):

    r = []
    s = sorted(a, key=lambda x: x[0])
    i = 0
    while i < len(s):
        r.append(s[i])
        while i < len(s)-1 and s[i][1] >= s[i+1][0]:
            r[-1][0] = min(r[-1][0], s[i+1][0])
            r[-1][1] = max(r[-1][1], s[i+1][0])
            i += 1
        i += 1
    return r

'''
r: []
s: [[1,2],[3,5],[4,7],[6,8],[9,10]]
      0     1     2     3     4
i: 0
while 0 < 4:   (0..3)
    r: [1,2]   current: [1,2]
    while 2 >= 3: -> False
    i: 1
    r: [1,2][3,5]  current: [3,5]
    while 5 >= 4: -> True
        a[3,5]: min(3,4) -> 3
        a[3,5]: max(5,7) -> 7   a[3,7]
        i: 2
    while 7 >= 6: -> True
        a[4,7]: min(4, 6) -> 6
        a[4,7]: max(6, 8) -> 8  a[3,8]
        i: 3
    while 8 >= 9: -> False
    i: 4                                     -->  i+=1  works because, in the inner while we are comparing current with nextItem
    r: [1,2][3,8][9,10]      
'''

a = [[4,7],[6,8],[9,10],[3,5],[1,2]]
print(mergeIntervals(a))