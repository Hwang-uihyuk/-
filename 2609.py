r = 1000000

check = [True for _ in range(6)]

for i in range(2, int(r**0.6)):
    if check[i] == True:
        for j in range(i*2, r, i):
            if check[j] == True:
                check[j] == False