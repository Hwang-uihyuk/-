t = int(input())
# 테스트 케이스 설정해주고 

for i in range(t):
    k = int(input())
    n = int(input())
    # 몇층 몇호에 사는지 적어주고 

    people = []
    for i in range(1,n+1):
        people.append(i)

    #people이라는 데이터에 1부터 호까지의 갯수를 적어주고 

    for x in range(k):
        for y in range(1,n):
            people[y] = people[y] + people[y-1]
            # y는 1부터 

    print(people[-1])
    # 0층의 1호 1명 
    # 0층의 2호 2명
    # 0층의 3호 3명

    # 1층의 1호 1명
    # 1층의 2호 1+2 = 3
    # 1층의 3호 1+2+3 = 6

    # 2층의 1호 1명 
    # 2층의 2호 1+1+2 = 4 
    # 2층의 3호 1+1+2+1+2+3 = 10

