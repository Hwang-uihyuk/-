n = int(input())
res = n
if n == 0:
        res = 1
else:
    for i in range(1,n):

        res = res*(n-i)
  

print(res)