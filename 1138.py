n = int(input())
data = []
data = list(map(int,input().split()))
print(data)
# 추가는 완료했고 이제부터 시작임

# 리스트를 0으로 초기화
res = [0 for i in range(n)]

tmp = [0 for i in range(n)]

for i in range(n):
    res[data[i]] = i+1
    res.pop(data[i])
    
    print(res) 