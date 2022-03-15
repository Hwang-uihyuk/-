from re import L


n,m = map(int,input().split())

arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))

k = int(input())

for _ in range(k):
    nl = list(map(int,input().split()))
    for x,y in arr:
        print(x,y)