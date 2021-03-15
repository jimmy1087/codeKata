def fib(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    if memo.get(n) is None:
        memo[n] = fib(n-2) + fib(n-1)
    return memo[n]

print(fib(7))
