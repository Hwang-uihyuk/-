n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((int(input_data[0]),int(input_data[1])))

array.sort(key = lambda num:(num[1],num[0]))

for num in array:
    print(num[0],num[1])