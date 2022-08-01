
s = [0,1,3]

# <1일때 0> , <2일때 1> , <2일때 2> <3일 때 3> <4일떄 5>

for i in range(3,1001):
    s.append(s[i-1] +s[i-2]*2)
n = int(input())
print(s[n] % 10007)
