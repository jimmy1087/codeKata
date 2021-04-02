'''
Write a function that takes in an array of positive integers and returns the maximum sum
of non adjacent elements in the array
'''

def maxSubsetSumNoAdjacent(a):

    if len(a) == 0:
        return 0

    if len(a) == 1:
        return a[0]

    if len(a) == 2:
        return max(a[0], a[1])

    dp = [0 for _ in range(len(a))]
    dp[0] = a[0]
    dp[1] = max(a[0], a[1])
    for i in range(2,len(a)):
        dp[i] = max(dp[i-1], dp[i-2] + a[i])

    return dp[-1]

a = [75, 105, 120, 75, 90, 135]
print(maxSubsetSumNoAdjacent(a), 330)

'''
a  = [75, 105,  120,         75,         90,          135          ]
dp = [75  105*  120+75:195*  75+105:180  90+195:285*  135+195:330* ] 
       -   75   105          195*        195          285          
Return = 330
'''

a = [10, 0, 20, 25, 15, 5, 30]
print(maxSubsetSumNoAdjacent(a), 75)

'''
a  = [10, 0,   20,        25,        15,        5,       30        ]
dp = [10  0    20+10:30*  25+10:35*  15+30:45*  5+35:40  30+45:75* ]
      -   10*  10         30         35         45*      45        

'''
