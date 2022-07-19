from tokenize import group


n = int(input())   # n을 받아주고 

group_word = 0
for _ in range(n):   # 반복문을 n 만큼 돌려주고
    word = input()   # word 값을 받아주고
    error = 0 
    for index in range(len(word)-1):   # 이중 for문 ?
        if word[index] != word[index+1]:
            new_word = word[index+1:] # new_word는 word[index+1] 만큼 새로운 단어가 된다.
            if new_word.count(word[index]) > 0:  #핵심인데 word[index]의 단어가 0개 이상이면 error를 추가해준다.
                error +=1
    if error == 0:
        group_word += 1 


print(group_word)
            #새로운 단어가 된다음에는 
