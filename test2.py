import sys
input = sys.stdin.readline

n = int(input())
stack = []

def push(x):
    stack.append(x)
def pop():
    if not stack:
        return -1
    return stack.pop()
def size():
    return len(stack)
def empty():
    if not stack:
        return 1
    return 0

def top():
    if not stack:
        return -1
    return stack[-1]

for _ in range(n):
    command = input().split()
    if 'push' in command :
        push(command[1])
    elif 'top' in command:
        print(top())