n = int(input())
result = 0

if (n - 1) % 8 == 0:
    result = 1
elif n % 8 == 0 or (n - 2) % 8 == 0:
    result = 2
elif (n - 3) % 4 == 0:
    result = 3
elif (n - 4) % 2 == 0:
    result = 4
elif (n - 5) % 8 == 0:
    result = 5

print(result)