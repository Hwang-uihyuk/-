N = int(input())

p = [0] + list(map(int,input().split()))
# 입력받은 값들
dp = [False for _ in range(N+1)]
# dp리스트에 있는 값들에 false를 다 넣어준다.
for i in range(1, N+1):
    for k in range(1, i+1):
        if dp[i] == False :
            dp[i] = dp[i-k]+p[k]
            print(dp)
        else :
            dp[i] = min(dp[i], dp[i-k]+p[k])
            print(dp)

print(dp[N])