#  사람들은 1,2,3 의 연속된 번호로 각각 표시된다.

# 1. 입력 파일의 첫째 줄에는 전체사람의 수n이 주어지고
# 2. 촌수를 계산해야 하므로 두 사람의 번호가 
# 3. 에는 부모 자식들 간의 관계수의 m이 주어진다
# 4. 부모 자식간의 관계 x,y 각 줄

import sys 
from collections import deque
input = sys.stdin.readline

short = lambda x:(x[0],x[1])
def bfs(p1,p2):
    cnt  = 0
    queue = deque([[p1,cnt]])
    while queue :
        v1,cnt = short(queue.popleft())
        if v1 == p2:
            return cnt
        if not visited[v1]:
            cnt +=1
            visited[v1]:
            for i in parent[v1]: