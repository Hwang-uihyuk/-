from collections import Counter
n = int(input())

data = []

for i in range(n):
    data.append(int(input()))

print(round(sum(data)/n)) # 소수점 이하 첫째 자리에서 반올림한 값을출력
data.sort()

if n == 1:
    print(data[0])
    print(data[0])
    print(0)
    exit()

print(data[n//2]) # 중앙값 



# 최빈값
cnt = Counter(data)
cnt = sorted(cnt.items(),key=lambda x:(-x[1],x[0]))
if cnt[0][1] == cnt[1][1] :
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(data[n-1]-data[0]) # 범위 