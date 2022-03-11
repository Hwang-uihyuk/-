n = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))
res = 0 

min_price = price[0]

for i in range(n-1):
    if price[i] <  min_price:
        min_price = price[i]

    res = res + min_price * distance[i]

print(res)