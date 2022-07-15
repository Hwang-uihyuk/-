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
                                    #이진 탐색은 sort된 상태에서 해야한다.
def binary_search(array,start,end):   # def binary_search(array,start,end):
    while start <= end:             # 반복문일때는 while start<end일때만 가능하다.
        mid = (start + end) // 2    # mid = (start + end) // 2
        current = array[0]          # current = array[0] 현재값이 current 값이다.
        count = 1   # count = 1이다.

    for i in range(1,len(array)): #1부터 길이만큼 for문 돌려주는데
        if array[i] >= current + mid : # array[i]가 currnet + mid 면 
            count += 1 # count = count + 1 하나씩 할때마다 증가한다.
            current = array[i]  #array[i]는 current 값이다.

        if count >= c:   #  count  값이 c 보다 크거나 같으면
            global answer  # 글로벌 answer
            start = mid + 1 # start가 미드값 + 1 이 된다.
            answer = mid  # mid랑 answer이 같다고 둔다.
        else:
            end = mid -1 # end = mid - 1

start = 1
end = array[-1] - array[0]
answer = 0

binary_search(array,start,end)
print(answer)