import sys
input = sys.stdin.readline

data = list(input().strip()) #abcd
n = int(input()) # 3 
cursor  = len(data) #커서 현재위치
for _ in range(n):
    edit = input().strip()
   
    if edit[0] == 'L':
        if cursor != 0: 
            cursor -= 1
    elif edit[0] == 'D':
        if cursor != len(data)+1 :
            cursor += 1
    elif edit[0] == 'B':
        if cursor != 0:
            del data[cursor-1]
            cursor -= 1
    elif edit[0] == 'P':
        data.insert(cursor, edit[1]) 
        cursor += 1
print("".join(data))
