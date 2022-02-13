#  "알고리즘 이론"



BFS 예제

from collections import deque

def bfs(graph, start, visited):
  #큐 구현을 위해 deque 라이브러리 사용
  queue = dequeue([start])
  # 현재 노드를 방문 처리 
  visited[start] = True 
  while queue:data = []
for i in range(10):
    data.append(int(input()))



print(int(sum(data)/10))
print(max(data, key = data.count))
    
    
<음료수 얼려 먹기>

n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))
    
def dfs(x,y):
  if x <= -1 or x >=n or y <= -1 or y >=m 
  # 주어진 장소를 벗어나는 순간
    return False
  if graph[x][y] == 0:
     graph[x][y] == 1
     dfs(x-1,y)
     dfs(x,y-1)
     dfs(x+1,y)
     dfs(x,y+1)
     return True
   return False
   
   
 result = 0
 for i in range(n):
    for j in range(m):
      if dfs(i,j) == True :
            result += 1
 print(result)
 
 
 <미로 탈출>
 from collections import deque 
 
 n,m = map(int,input().split())
 for i in range(n):
      graph.append(list(map(int,input())))
      
 dx = [-1,1,0,0]
 dy = [0,0,-1,1]
 
 def bfs(x,y)
     queue = deque()
     queue.append((x,y))
     while queue:
     x,y = queue.popleft()
     for i in range(4):
         nx = x + dx[i]
         ny = y = dy[i]
         
         if nx < 0 or ny < 0 or nx >= n or ny >=m:
              continue
         if graph[nx][ny] == 0 :
              continue
         if graph[nx][ny] == 1:
              graph[nx][ny] = graph[x][y] + 1
              queue.append((nx,ny))
         return graph[n-1][m-1]
         
  print(bfs(0,0))
  
  
  
  
  
  
  
 
