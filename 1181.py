import sys

n = int(sys.stdin.readline())

data = []
for i in range(n):
    data.append(sys.stdin.readline().strip())
set_data= set(data)
data = list(set_data)
    # set함수를 쓴다음 다시 list로 변경해야 sort할 수 있다.
data.sort()
    # 먼저 sort를 진행해주는 이유는 
    # 같은 길이여도 뭐가 더 빨리 나오느냐에 따라 sort 되기 때문이다.

data.sort(key = len)

for j in data:
   print(j)
# 중복제거해주고 



