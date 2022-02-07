n = int(input())
data = list(map(int,input().split()))

result = 0
sum = 0

for i in range(n):
    if data[i] == 1:
        sum = sum + 1
        result = result + sum
    else :
        sum = 0

print(result)
