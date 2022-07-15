n,k = map(int,input().split()) # 첫번째 n에서 -1을한다.
                               # 두번째 n에서 k로 나눈다.

data = 0

while n != 1:               #1이 아니라면 반복문 실행
    if n%k == 0:            #만약에 n을 k로 나눈 나머지가 0이라면 나눠준다. 그리고 횟수를 한 번 추가해준다.
        n = n//k
        data = data + 1
    else:
        n = n -1
        data = data + 1

print(data)

