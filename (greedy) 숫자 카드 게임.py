n,m = map(int,input().split()) # n,m 행렬을 만들어주고 그 수 만큼 받아준다.
min_num = -10001 

for i in range(n):
    data = list(map(int,input().split()))  # 한줄씩 입력받을때 각 줄의 최솟값들을 비교해서 그 최솟값들 중에 가장 큰 값을 구하자.
    if min_num < min(data):                                        # 예를들어 2 3 4 라고 했을때
        min_num = min(data)


print(min_num)