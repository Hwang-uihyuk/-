def dfs(graph,v,visited):
    visited[v] = True
    #방문했으면 방문처리해줌.
    print(v,end='')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

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
# 노드 8갠데 일부러 크게하나 해줌 이유는 ??

visited = [False] * 9 
dfs(graph,1,visited)