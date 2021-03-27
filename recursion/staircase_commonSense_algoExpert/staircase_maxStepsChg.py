def numberOfPaths(staircase, maxSteps, algoSteps):
    algoSteps['steps'] += 1
    if staircase <= 1:
        return 1
    totalSteps = 0
    for i in range(1, maxSteps+1):
        totalSteps += numberOfPaths(staircase - i, maxSteps, algoSteps)
    return totalSteps

algoSteps = { 'steps': 0 }
print(numberOfPaths(20,3, algoSteps))
print('Number of steps in recursion call', algoSteps['steps'])


def numberOfPathsMemoization(staircase, maxSteps, algoSteps, m = {}):
    algoSteps['steps'] += 1
    if staircase in m:
        return m[staircase]
    if staircase <= 1:
        return 1
    totalSteps = 0
    for i in range(1, maxSteps+1):
        totalSteps += numberOfPathsMemoization(staircase - i, maxSteps, algoSteps, m)
    m[staircase] = totalSteps
    return totalSteps

algoSteps = { 'steps': 0 }
print(numberOfPathsMemoization(20,3, algoSteps))
print('Number of steps in recursion call with Memo', algoSteps['steps'])


