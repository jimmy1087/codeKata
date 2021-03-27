'''
Let’s say we have a staircase of N steps, and a person has the ability to climb one, two, or three steps at a time. 
How many different possible “paths” can someone take to reach the top? 
Write a function that will calculate this for N steps.

ie1)   staircase of 5 steps would be

1)  1 1 1 1 1
2)  1 1 1 2
3)  1 1 2 1
4)  1 2 1 1
5)  2 1 1 1
6)  2 2 1
7)  2 1 2
8)  1 2 2 
9)  1 1 3
10) 1 3 1
11) 3 1 1 
12) 2 3
13) 3 2

'''

def numOfPathsExplicit(n):
    if n < 0: return 0
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4
    return numOfPathsExplicit(n-1) + numOfPathsExplicit(n-2) + numOfPathsExplicit(n-3)

print(numOfPathsExplicit(5))


def numOfPaths(n):
    if n < 0: return 0
    if n == 1 or n == 0: return 1
    return numOfPaths(n-1) + numOfPaths(n-2) + numOfPaths(n-3)

print(numOfPaths(5))


