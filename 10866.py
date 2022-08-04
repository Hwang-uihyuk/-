from collections import deque
import sys


n = int(sys.stdin.readline())
deque = deque()
for i in range(n):
    data = list(map(str,sys.stdin.readline().split()))
    if 'push_front' in data:
        deque.appendleft(data[1])
    elif 'push_back'in data:
        deque.append(data[1])
    elif 'pop_front' in data:
        if not deque:
            print(-1)
        else: print(deque.popleft())
    elif 'pop_back' in data:
        if not deque:
            print(-1)
        else : print(deque.pop())
    elif 'size' in data:
        print(len(deque))
#         push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif 'empty' in data:
        if not deque:
            print(1)
        else: print(0)
    elif 'front' in data:
        if not deque:
            print(-1)
        else :print(deque[0])
    elif 'back' in data:
        if not deque:
            print(-1)
        else:print(deque[-1])

