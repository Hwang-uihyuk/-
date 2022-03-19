n = int(input())

data = 0
if n%3 == 0:
    if n//5 >= 3:
        data = n//5
        n = n%5

    if n%3 == 0:
        data = data + n//3 
        n = n%3


# 이제 11 같은 수는 어떻게 해결할가 ?
# 5 => 1번 
# 3=>2 번
# 13같은거는 5=> 2번 3=>1번
# 14같은거는 5 => 1번 3=>3번
# 그러면 5랑 3에 아무거나 곱해서 
# 도 
if n//5 >=3:
    data = data + n//5
    n = n%5




if n!= 0:
    print("-1")
elif n == 0:
    print(data)
