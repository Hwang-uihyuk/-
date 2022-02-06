t = int(input())
# t가 400이라고 가정해보자

# a는 5분 = 300초 // b는 1분 = 60초 c는 10초
atmp =0
btmp =0
ctmp =0
if t>= 300 :
    # t가 300보다 크므로 
    
    # t를 300으로 남기고난 걸 t에 대입해주고
    # 이제 t는 100이다
    atmp = atmp + t//300
    t = t%300
    # 300초일떄의 tmp는 t나누기 300이다   
    # 400//300 = 1 이다. 즉, atmp = 1
    

if t>= 60 :
    #t가 100이므로 
    btmp = btmp+t//60
    t = t%60

if t>= 10:
    
    ctmp = ctmp+t//10
    t = t%10
if t>0:
    print("-1")
     
if t == 0:
    print(atmp,btmp,ctmp)