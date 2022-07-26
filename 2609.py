#최대공약수 최소공배수 문제는
#1번 풀이법 :
# 유클리드 호재법과
#2번 풀이법 :
# 내장된 함수 gcd,lcd로 풀 수 있다.
#3번 풀이법 :
# for문과 while문을 이용해서 풀 수 있다.

#1번 풀이법 - >

a,b = map(int,input().split())
aa,bb = a,b # a,b의 값을 보존하기 위해

# a,b의 순서가 달라도 계산하다보면 둘이 같아진다.

while bb != 0: #b가 0이 아닐때는 돌려라
    aa = aa%bb 
    aa,bb = bb,aa


# aa는 최대공약수가 된다.
lc = a*b // aa

print(aa)
print(lc)

