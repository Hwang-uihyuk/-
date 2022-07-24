for i in range(n,2*n+1):
    if i==1:
       continue
    for j in range(2,int(n ** 0.5)+1):
      if i%j == 0:    
        cnt += 1
        break
        else:

    print(cnt)
            

        
        
