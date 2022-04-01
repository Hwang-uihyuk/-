from collections import deque

def bfs(graph,start,visitied):
    queue = deque([start])

    visitied = True
    while queue:
        v = queue.popleft()
        print(v,end='')
        for i in graph[v]:
            if not visitied[i]:
                queue.append(i)
                visitied = True
graph = [
    [],
    [2,3,8],    # 그래프의 노드와 연결된 것을 표시하는듯?
    [1,7],
    [1,4,5],
    [3,4],
    [3,5],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9 

bfs(graph,1,visited)