n = int(input())

data = []
for i in range(n):
    data.append(int(input()))

data.sort()

for j in range(n):
    print(data[j])