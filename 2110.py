#array라는 리스트에 집들이 좌표를 입력받은 후에 정렬
# start = 1 end = array[-1]-array[0] 시작값은 최소 거리// 끝 값은 최대거리
# 앞 집부터 공유기 설치
# 설치할 수 있는 공유기 개수가 c개를 넘어서면 더 넓게 설치할 수 있다는  
# 이야기 이므로 설치거리를 mid + 1로 설정하여 다시 앞집부터 설치
# c개를 넘어가지 않는다면 더 좁게 설치해야 한다는 이야기 이므로 mid -1 설정.

n,c = map(int,input().split())

array = []
for i in range(n):
    array.append(int(input()))

array.sort()

def binary_search(array,start,end):
    while start <= end:
        mid = (start + end) // 2
        current = array[0]
        count = 1

    for i in range(1,len(array)):
        if array[i] >= current + mid :
            count += 1
            current = array[i]

        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid -1

start = 1
end = array[-1] - array[0]
answer = 0

binary_search(array,start,end)
print(answer)