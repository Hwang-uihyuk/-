from curses.ascii import isalpha, islower
from ntpath import join


datas = input()

stack = []

for data in datas:
    if data.isupper():
        if ord(data)+13 >= 91:
            stack.append(chr(ord(data)+13-26))
        else:
            stack.append(chr(ord(data)+13))
    elif data.islower():
        if ord(data)+13 >=123:
            stack.append(chr(ord(data)+13-26))
        else:
            stack.append(chr(ord(data)+13))
    else:
        stack.append(data)
print(*stack, sep="")
