
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
    if len(stack) == 0:
        return 1
    else:
        return 0

def top():
    return stack[-1]

for _ in range(n):

    n = int(input())
    rs = input().split()

    if rs[0] == 'push':
        push(rs[1])

    elif rs[0] == 'pop':
        print(pop())
    elif rs[0] == 'size':
        print(size())
    elif rs[0] == 'empty':
        print(empty())
    elif rs[0] == 'top':
        print(top())
        

