def golomb(n, steps):
    steps[0] += 1
    if n == 1: return 1
    return 1 + golomb(n - golomb(golomb(n - 1, steps), steps), steps)

steps = {0:0}
print(golomb(30, steps))
print(steps)



def golomb_dp(n, steps, memo = {}):
    steps[0] += 1
    if n == 1: return 1
    if memo.get(n) is None:
        memo[n] = 1 + golomb_dp(n - golomb_dp(golomb_dp(n - 1, steps, memo), steps, memo), steps, memo)
    return memo[n]


steps = {0:0}
print(golomb_dp(30, steps))
print(steps)