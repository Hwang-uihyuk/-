import sys
n = int(input())                                # n이 4고
A = list(map(int, sys.stdin.readline().split())) # A의 list가 3 5 2 7일 때

answer = [-1] * n                               #answer에 -1을 넣어주는 이유는 더 큰 것이 없을때에 -1을 출력해주어야 하기 떄문이다.
stack = []                                      #빈 stack


stack.append(0)                                 #0을 넣어준다. stack = ["0"] 현재 상황


for i in range(1, n):                           #1부터 3까지 돌려준다.

    while stack and A[stack[-1]] < A[i]: # stack이 비어있지 않고 // A[0] < A[1] 이 더 클때 
        answer[stack.pop()] = A[i]       # anwser 리스트에서 0을 지우고  그 값에 A[1] == 5를 집어넣는다. 
    stack.append(i)                      # stack에 1을 집어넣는다.


print(*answer)                           # list 앞에 *을 붙히면 그냥 숫자가 나타난다.