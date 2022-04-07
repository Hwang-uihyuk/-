expression = input().split('-')
for i in range(len(expression)):
    if '+' in expression[i]:
        expression[i]= sum(map(int,expression[i].split('+')))
    else:
        expression[i] = int(expression[i])
print(expression[0] - sum(expression[1:]))

#주어지는 수식을 최대한 작은 수로 만들어야한다.
#작은수로만드는법 뺄셈 연산자 사이의 수들을 모두 더한다.
#그 수들을 가장 앞에 있는 수와 뺀다.
#.