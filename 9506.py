
while True :
    n = int(input())
   
    if n == -1: 
        break
    data = []
    for i in range(1,n):
        if n%i == 0:
            data.append(i)
    if sum(data) == n:
       

        print(n, "=" ," + ".join(str(i) for i in data))
    else :
        print(n, "is NOT perfect.")
        
