N = int(input())                         #n에서 4를 대입하고
p = [0] + list(map(int,input().split())) #계산하기 쉽게 p[0] = 0 대입해주고 나머지에 나머지 숫자
                                         #대입한다.  p = [0, 1, 5, 6, 7]
dp = [0 for _ in range(N+1)]             # dp = [0,0,0,0]


for i in range(1,N+1):                   # 이중 for문
    for k in range(1,i+1):
        dp[i] = max(dp[i], dp[i-k] + p[k])  #dp[1] = max(dp[1],dp[0] + p[1])
print(dp[i])                                    