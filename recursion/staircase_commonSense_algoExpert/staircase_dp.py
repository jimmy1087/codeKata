def numberOfWays(height, maxSteps):

    dp = [0 for _ in range(height + 1)]

    dp[0] = 1
    dp[1] = 1

    for curHeight in range(2, height + 1):
        step = 1
        while step <= maxSteps and step <= curHeight:
            dp[curHeight] += dp[curHeight - step]
            step += 1

    print(dp)
    return dp[height]

print(numberOfWays(20,3))