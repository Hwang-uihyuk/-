n = int(input())

res = 0

for i in range(n):
    n = n - i
    res = res + 1
    if n < i:
        print(res)
    