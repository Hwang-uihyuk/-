# 너비 우선 탐색이고 가까운 노드부터 탐색한다. 
# dfs와 bfs의 차이
# dfs는 최대한 멀리있는 노드부터 탐색하는데 bfs는 가까운 노드부터 검색한다. becasue of queue
# dfs는 2번으로 들어갔으면 거기서 계속 탐색하는데
# bfs는 나를 기준으로 가까운 곳들을 먼저 탐색 할 수 있다.

from collections import deque

# bfs메서드 정의
def bfs(graph,start,visited):
    queue = deque[start]
    # 첫번째 들어가는걸 큐에 넣어준다.?
    visited[start] = True
    # 큐가 빌때까지 방문 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력 
        v = queue.popleft()
        print(v,end='')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited = [True]


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

vistied = [False] * 9 

bfs(graph,1,vistied)
