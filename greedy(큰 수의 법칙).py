from calendar import month_name
from importlib.util import MAGIC_NUMBER


n,m,k = map(int,input().split())  # n => 적을 갯수 m => 더할 갯수 k => 최대로 더할 수 잇는 갯수
data = list(map(int,input().split()))
data.sort(reverse=True)
# n이 5이고 2 4 5 4 6 = > 6 5 4 4 2  
# m은 8  8개를 더해라.
# k는 3  결국에는 data[0] 과 data[1] 만 필요하다.

res = 0

while True:
    for i in range(k):
        if m == 0:
            break
        # m 이 0 이라면 break해주고
        # 아니라면 res 값에 가장 큰 값을 더해준다.
        
        res = res + data[0]
        m -= 1
    if m == 0:
        break 
        # m이 얼마 안남고 k가 더 클때 중간에 끊길 경우를 대비
        
    res = res + data[1] # 한 번 더해주면 다시 가장 큰 값으로 더 해 줄 수 있으므로 while 문을 사용하였음
    m -= 1 # 그래서 while -> for 문 처음에 if == 0 이면 break를 해준다.

print(res)




