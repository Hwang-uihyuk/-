import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr2 = []
print(arr)
arr2 = list(sorted(set(arr)))

print(arr2)
dic = {arr2[i]:i for i in range(len(arr2))}
print(dic)

for i in arr:
    print(dic[i],end=' ')