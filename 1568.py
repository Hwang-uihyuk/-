n = int(input())

res = 0
k = 1

while n > 0:
    if n < k:
        k = 1
    n = n -k
    k += 1
    res = res + 1
print(res)

    