n = int(input())   #n=10

dp = [0 for _ in range(n+1)] # 그냥 빈공간에 숫자 넣어주기 dp = [0,0,0,0,0,0,0,0,0,0,0,0,0] 11개



for i in range(2, n+1) :  #2부터 10까지 i에 넣어준다.
    dp[i] = dp[i-1] + 1     #dp[3] = dp[2] + 1
    print(dp)    
    if i%2 == 0 and dp[i] > dp[i//2] + 1 : #d는 결과가 아닌 계산한 횟수를 저장하는 것
        dp[i] = dp[i//2]+1                 # 2%2 == 0 and dp[2]>dp[1] + 1
    if i%3 == 0 and dp[i] > dp[i//3] + 1 : # 
        dp[i] = dp[i//3]+1

print(dp[n])