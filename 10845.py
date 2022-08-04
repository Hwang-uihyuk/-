from multiprocessing.context import ForkContext
import sys
input = sys.stdin.readline()


queue = []

def push(x):
    queue.append(x)
    
def pop():
    if not queue :
        return -1
    return queue.pop(0)
def size():
    return len(queue)

def empty(): 
    if not queue :
        return 1
    else:
        return 0
def front():
    if not queue:
        return -1
    return queue[0]
def back():
    if not queue:
        return -1
    return queue[-1]

n = int(input())

for i in range(n):
    data = input().split()
    if data[0] == 'push':
        push(data[1])
    elif data[0] == 'pop':
        print(pop())
    elif data[0] == 'size':
        print(size())
    elif data[0] == 'front':
        print(front())
    elif data[0] == 'back':
        print(back())
    elif data[0] == 'empty':
        print(empty())