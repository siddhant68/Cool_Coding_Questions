# recursive with number of steps = 2
def no_of_stairs(n):
    if n == 0:
        return 1
    
    if n < 0:
        return 0
    
    return no_of_stairs(n-1) + no_of_stairs(n-2) + no_of_stairs(n-3)

# recursive with number of steps
def no_of_stairs_steps(n, k):
    if n == 0:
        return 1
    
    if n < 0:
        return 0
    
    ans = 0
    for i in range(1, k+1):
        ans += no_of_stairs_steps(n-i, k)
    return ans

# dp bottom up
def no_of_stairs_dp_bu(n, k):
    dp = [-1] * (n+1)
    dp[0] = 1
    
    for i in range(1, n+1):
        dp[i] = 0
        for j in range(1, k+1):
            if i-j >= 0:
                dp[i] += dp[i-j]
    return dp[n]

print(no_of_stairs_dp_bu(4, 3))
print(no_of_stairs_dp_bu(5, 4))
