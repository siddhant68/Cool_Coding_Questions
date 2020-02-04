# recursion
def fib(n):
    if n == 0 or n == 1:
        return n
    
    return fib(n-1) + fib(n-2)

# dynamic programming top down
def fib_top_down(n, dp):
    if n == 0 or n == 1:
        dp[n] = n
        return n
    
    if dp[n] != -1:
        return dp[n];
    else:
        dp[n] = fib(n-1) + fib(n-2)
        return dp[n]

# dynamic programming bottom up
def fib_bottom_up(n):
    dp = [-1] * (n+1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, len(dp)):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

print(fib_bottom_up(5))