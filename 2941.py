# 먼저 크로아티아 넘버를 적어준다.
word = ['c=', 'c-', 'dz=', 'd-', 'lj','nj','s=','z=']

res = input()

for x in word:
    res = res.replace(x, '*')



print(len(res))