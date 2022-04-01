from collections import deque

n,m,v = map(int,input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    m1,m2 = map(int,input().split())
    graph[m1][m2] = graph[m2][m1] = 1

def bfs(start_v):
    discoverd = [start_v]
    queue = deque()
    queue.append(start_v)

    while queue:
        v = queue.popleft()
        print(v,end=' ')
    