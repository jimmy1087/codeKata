'''
https://app.codesignal.com/arcade/graphs-arcade/kingdom-roads/nCMisf4ZKpDLdHevE/solutions?solutionId=rubW82sSG8nuvn4CL
Each city has the same number of incoming and outgoing roads. As the Hand of the King, you're the one who he has decreed must check his calculations.

input:

    (0) ---* (1)
     *      /
     |     /
     |    /
     |   /
     |  *
    (2) *--* (3)

        0   1   2   3
    0       *
    1           *
    2    *          *
    3           *

-----
    o(n^2) time:

    Loop (i-Rows = 0)
    i   j   roadsPerCity        0   1   2   3
    0   1       +1          0   ----*-------->
    2   0       -1          1   |
                            2   *
                            3   |
                                v

    Loop (i-Rows = 1)           0   1   2   3
    0   1       -1          0       *
    1   2       +1          1   ----|---*----->
                            2       |
                            3       |
                                    v

    Loop (i-Rows = 2)           0   1   2   3
    2   0       +1          0           |
    1   2       -1          1           *
    2   3       +1          2   *-------|---*->
    3   2       -1          3           *
                                        v

    Loop (i-Rows = 3)           0   1   2   3
    3   2       +1          0               |
    2   3       -1          1               |
                            2               *
                            3   --------*---|->
                                            v
'''                 

def newRoadSystem(roads):

    for i in range(len(roads)):
        roadsPerCity = 0
        for j in range(len(roads[i])):

            if roads[i][j]:
                roadsPerCity += 1
                print('i:', i, '  j:', j, '  +1: ', roadsPerCity)
            if roads[j][i]:
                roadsPerCity -= 1
                print('j:', j, '  i:', i, '  -1: ', roadsPerCity)

        if roadsPerCity > 0:
            return False

    return True

roadRegister= [ [False,True,False,False], 
                [False,False,True,False], 
                [True,False,False,True], 
                [False,False,True,False] ]

print(newRoadSystem(roadRegister))