n = int(input())      #첫번째는 공간을 만들어준다.
datas = input().split()   #data에 L,R,U,D 좌우상하로 옮길 수 있다.
x,y = 1,1                #x,y에 초기값 1,1을 넣어준다. 옮기면서 더해줘야 하기 때문에

dx = [0,0,-1,1]          # if L을 입력한다면 
dy = [-1,1,0,0]
moving = ['L','R','U','D']

for data in datas:
    for i in range(len(moving)):
        if data == moving[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n :
          continue
x,y  = nx, ny

print(x,y)
