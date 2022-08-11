



import sys


# 끝나는게 정해져 있지 않으니
# for문과 while문의 차이점 while문은 
n = 0
while n<100 :
    n += 1
    datas = list(sys.stdin.readline().rstrip('\n'))
     
    if not datas:



        break

    lower,upper,num,space = 0,0,0,0
    for data in datas:
        if data.islower():
            lower += 1
        elif data.isupper():
            upper += 1
        elif data.isdigit():
            num += 1
        else:       
            space += 1 
    
    print(lower, upper, num, space)