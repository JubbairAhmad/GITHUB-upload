def climbStairs(n,dp ={}):
    if n <= 1:
        return n
    if n not in dp:
        dp[n] = climbStairs(n + 1,dp) + climbStairs(n + 2,dp)
    return dp[n]

n = int(input())
print(climbStairs(n,{}))