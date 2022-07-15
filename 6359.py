t = int(input())
n = []

for i in range(t):

    n = int(input())

    answer = 0

    for i in range(1,n):

        if i**2 <= n:

            answer += 1

        if i**2 > n:

            break
        
    print(answer)
    # 기숙사의 지하에는 n개의 일렬로 늘어선 감옥이 있다.
    # 각 방에는 벌점을 많이 받은 학생이 구금되어있다.
    #  ㅁ(1)   ㅁ(2)  ㅁ(3)  ㅁ(4)  ㅁ(5)  ㅁ(6)  ㅁ(7)  ㅁ(8)
    #   