n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((int(input_data[0]),input_data[1]))

array = sorted(array,key=lambda num:num[0])

for j in array:
    print(j[0],j[1])







