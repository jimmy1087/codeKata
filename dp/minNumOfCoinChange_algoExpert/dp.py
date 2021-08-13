# Return the smallest number of coins needed to reach a target
# n = Target
# denominations = coin denominations

# o(nd) time || o(n) space
def minNumOfCoinChange(n, denominations):

    ways = [float('inf') for _ in range(n+1)]
    ways[0] = 0

    for amount in range(n+1):
        for denom in denominations:
            if denom <= amount:
                ways[amount] = min(ways[amount], 1 + ways[amount-denom])
    
    return ways[n] if ways[n] < float('inf') else -1


t = 7
denominations = [1,5,10]

print(minNumOfCoinChange(t, denominations))

# ways[0] = 0
# ways[1] = 1, 2, 3, 4, 5, 6, 7      when using coins of 1, each amount up to 7 requires the same number of coins
# ways[5] = -  -  -  -  1, 2, 3      when using coins of 5, at amount 5, we only need 1 coin, at 6 we need 1 of 5 + 1 of 1, at 7 1 of 5 and 2 of 1
                                     #ways[5] when 7 =    min ( ways[7] (currently is 7 coins of 1), 1 coin + ways[7-5=2] which is 1 + 2 = 3)
# ways[10]  -  -  -  -  -  -  -