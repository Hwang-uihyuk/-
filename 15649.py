n, m = map(int, input().split())
s=[]
s[0] = 1



def f():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return



  for i in range(1, n + 1):     # n = 4 이고 m = 2 라면
    if i in s:                  # 중복되면 멈추고
      continue
    if i < s[-1]:
        continue

    s.append(i)                 # 아니라면 s list에 append(i)
    f()
    s.pop()

f()