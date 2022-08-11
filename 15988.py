t = int(input())

dp = [1,2,4]
for i in range(t):
    n = int(input())
    for j in range(len(dp), n):
        dp.append(dp[j-3] + dp[j-2] + dp[j-1])
    