n = int(input())                            # n = 4
d = [0] * (n + 1)                           # d = [0,0,0,0,0]
p = [0] + list(map(int, input().split()))   # p = [0,1,5,6,7]
d[1] = p[1]                                 # d[1] = p[1]은 카드 한 장 일때니까 무조건 같다.
for i in range(2, n + 1):                   
    for j in range(1, i + 1):
        if d[i] < d[i - j] + p[j]: #만약 1_) d[2] < d[1] + p[1]  2_)  d[0] + p[2] 
            d[i] = d[i - j] + p[j] #
print(d[n])