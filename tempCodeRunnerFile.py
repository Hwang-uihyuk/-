n = int(input())

array= []
for i in range(n):
    i_data = input().split()
    array.append((int(i_data[0]),int(i_data[1])))
    
array = sorted(array,key = lambda a:(a[0],a[1]))

for j in array:
    print(j[0],j[1])
