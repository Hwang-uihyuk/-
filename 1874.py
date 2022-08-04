n = int(input())  # n이 몇번 계산할건지 test case
s = [] # 무슨 리스트인지 알아내기 

op = []  # + , - 를 넣어줄 리스트

count = 1 # count 왜 있는지 알아내기
temp = True  # 왜 true 값을 줬는지 ?
for i in range(n): #test case를 계산해야 해야 하기떄문에 for문을 돌림
    num = int(input()) # test case 만큼 int(input())

    while count <= num: # count는 num 보다 작거나 같을때 계속 while문
        s.append(count) # s리스트에 count를 넣어준다.
        op.append('+') # op리스트에는 +를 넣어준다.
        count += 1 # count에는 +1 을 해주고 대입해준다.
    if s[-1] == num: # 만약 가장 최근에 들어온 값과 num의 값이 같을때
        s.pop() # pop -> del 해주고 
        op.append('-') # op리스트에는 - 넣어준다.
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in op:
        print(i)