

# 유클리드 호재법으로 푼 최대공약수 
t = int(input())

for i in range(t):
        data = list(map(int,input().split()))
        total = 0
        for j in range(1,len(data)):
            for k in range(j+1,len(data)):
                aa,bb = data[j],data[k]                
                while bb != 0:
                    aa = aa%bb 
                    aa,bb = bb,aa

                    
                total = total + aa
        print(total)

