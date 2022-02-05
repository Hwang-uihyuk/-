t = int(input())

for i in range(t):
    n = int(input())
    max_res = 0
    for _ in range(n):
        a,b = input().split()
        b = int(b)
        if max_res < b:
            res_a = a 
            max_res = int(b)

    print(res_a)
    #restart