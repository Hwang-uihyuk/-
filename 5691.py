import sys
while True:
    a,b=map(int,sys.stdin.readline().strip().split())
    if a==0 and b==0:break
    print(min([2*a-b,2*b-a,(a+b)/2]))
    
