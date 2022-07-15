from turtle import end_fill

def binary_search(array,target,start,end):
    # in 재귀함수


    mid = (start + end)//2
    
    if start > end :
        return None
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start, mid-1)
    elif array[mid] < target:
        return binary_search(array,target,mid+1,end)

n = int(input())
array = sorted(list(map(int,input().split())))
m = int(input())
x = list(map(int,input().split()))

for i in x:
    result = binary_search(array,i,0,n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print("no", end=' ')