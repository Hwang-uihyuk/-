N = int(input())                         #n = 6

A = list(map(int, input().split()))      #10 20 10 30 20 50

dp = [1] * N                             # dp =[1,1,1,1,1,1] 계산횟수를 정해주는거고


for i in range(N):                       # if i가 1일 때
    for j in range(i):                   # j는 0이 대입된다.
        if A[j] < A[i]:                  # A[0] < A[1] 이면 dp[1] = max(dp[1],dp[0]+1) 
            dp[i] = max(dp[i],dp[j]+1)
            if (A[i]+1) <A[i]:    #### 여기 부분 부터 수정하면 됨.

                s.append(A[i])
print(max(dp))
print(s)
