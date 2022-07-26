import sys
input = sys.stdin.readline


def solve(n, k): #solve n,k를 받는다.
    if n == 0:
        return '0'
    else:
        if n % 2 == 0:  #2로 나눌떄 나머지가 0 이면 재귀함수로 계속돌려준다.
            return solve(n//k, k) + '0'
        else:
            return solve(n//k+1, k) + '1'


T = int(input())
ans = solve(T, -2)
if ans == '0':
    print(ans)
else:
    print(ans[1:])