n = int(input())

dp = [0 for _ in range(n+1)] # 그냥 빈공간에 숫자 넣어주기



for i in range(2, n+1) : 
    dp[i] = dp[i-1] + 1 
    print(dp)    
    if i%2 == 0 and dp[i] > dp[i//2] + 1 : #d는 결과가 아닌 계산한 횟수를 저장하는 것
        dp[i] = dp[i//2]+1
    if i%3 == 0 and dp[i] > dp[i//3] + 1 :
        dp[i] = dp[i//3]+1

print(dp[n])