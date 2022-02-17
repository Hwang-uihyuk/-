num = set(range(1,10001))
# {} 형태로 1부터 10000까지 데이터에 입력해줬다.
data = set()
# 이것도 {} 이 형태로 만들어줘야함

for i in range(1,10001):
    for j in str(i):
        # 문자열을 for문으로 사용하는 방법
        # 정수형은 이렇게 사용하지 못한다.
        i = i+int(j)
    data.add(i)

res = sorted(num-data)
for i in res:  
    print(i)
