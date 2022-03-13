a_info = list(map(int,input().split()))

b_info = list(map(int,input().split()))

a = sum(a_info)
b = sum(b_info)

if(a>=b):
    print(a)
else:
    print(b)
