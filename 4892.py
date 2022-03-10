n0 = 1
i = 0
while n0 != 0:
    
    i += 1
    n0 = int(input())
    if n0 == 0:
        break
    n1 = 3*n0
    if n1%2 ==0:
        n2 = n1/2
        nnn = "even"
    else:
        n2 = (n1+1)/2
        nnn = "odd"
    n3 = 3*n2
    n4 = n3/9

    print(str(i)+'.', nnn,int(n4))
