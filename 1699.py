import math
n = int(input())

count = 0

while n != 0:
    res = math.floor(n ** (0.5))
    
    n = n - (res**2)
    count += 1
    if n == 0:
        print(count)