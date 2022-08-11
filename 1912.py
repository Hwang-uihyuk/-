# n = int(input())

# arr = list(map(int, input().split()))
# dp = [0] * n
# dp[0] = arr[0]

# for i in range(1, n):
#     dp[i] = max(arr[i], dp[i-1] + arr[i]) #dp[1] = max(arr[1], dp[0] + arr[1] 

# print(max(dp))

n = int(input())

arr = list(map(int,input().split()))
dp = [0] * n 
dp[0] = arr[0]

for i in range(1,n):
    dp[i] = max(arr[i], dp[i-1] + arr[i])
    print(dp)
print(max(dp))


