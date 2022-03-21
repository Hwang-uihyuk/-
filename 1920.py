from sys import stdin, stdout
n = stdin.readline() #첫번째 줄 
N = sorted(map(int,stdin.readline().split())) #이진 탐색은 정렬해줘야해서 sorted로 리스트 받음
m = stdin.readline() #세번째 줄에 몇개를 받을건지
M = map(int,stdin.readline().split()) # 


# ㅣ은 M 리스트에 있는 요소들
def binary_search(l,N,start,end):
    if start > end :
        return 0
    m = (start + end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary_search(l,N,start, m-1)
    else:
        return binary_search(l,N,m+1,end)

# 재귀함수 이용해서 이진 탐색 활용하기

for l in M :
    start = 0
    end = len(N) - 1
    print(binary_search(l,N,start,end))