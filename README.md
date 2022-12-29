# Baekjoon



# JavaScript

- const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
    - 리눅스 환경일 때 아닐 때

### 2798 블랙잭

```jsx
var fs = require('fs')
var inputs = fs.readFileSync('./input.txt').toString().split('\n');
// split('\n'을 기준으로 나뉜다.)

var firstLine = inputs[0].split(" ")
// 첫번째 라인은 5 21
var secondLine = inputs[1].split(" ").map(item => parseInt(item))
// 두번째 라인은 5 6 7 8 9

var res = 0
//결과값을 저장해줄 변수

//세 개의 수를 뽑아서 21과 가장 근접한값을 뽑아야 함으로
//일일이 모든 경우의 수를 다 더해야 한다.
// 일명 : '브루트포스 알고리즘' 이라는것입니다.

//총 3개의 for문을 돌려줍니다.
//for문의 조건문에서는 i는 5개중 3번째 index까지만 가야 나머지 세가지의 수로 모든 경우의 수를 구할 수 있습니다.
for(var i = 0; i < parseInt(firstLine[0]-2); i++)
{
    for (var j =i+1; j< parseInt(firstLine[0]-1); j++) 
    {
        for (var k = j+1; k<parseInt(firstLine[0]); k++)
        {
            //조건문에서는 21보다 작거나 같고 // 세 수를 더 한 값이 결과값에 계속 저장을 해줌으로써 가장 근접한 수를 찾아냅니다.
            if( (secondLine[i]+secondLine[j]+secondLine[k]) <= firstLine[1] && res < secondLine[i]+secondLine[j]+secondLine[k])
            {
                res = secondLine[i]+secondLine[j]+secondLine[k]
                
            }
        }
    }
}
console.log(res)

```

### 

### 10988 팰린드롬인지 확인하기

```jsx
var fs = require('fs')
var filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
var input = fs.readFileSync(filepath).toString().trim();

console.log(input === input.split("").reverse().join("") ? 1: 0)

// 입력값이 : levelsdf 일때 
//split 까지만 쪼개면 ['l', 'e', 'v','e', 'l', 's','d', 'f']
//reverse 하면 ['f', 'd', 's','l', 'e', 'v','e', 'l']
//join 해주면 fdslevel
```


### 11057 오르막 수

```jsx
var fs = require('fs')
var filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
var input = fs.readFileSync(filepath).toString().trim()*1

let dp = Array.from(Array(input+1), ()=> []);

dp[1] = [1,1,1,1,1,1,1,1,1,1]
dp[2] = [1,2,3,4,5,6,7,8,9,10];
dp[3] = [1,3,6,10,15,21,28,36,45,55]
for(let i = 4; i<=input; i++){
    for(let j =0; j<10; j++){
        dp[i][j] = 0;
        for(let k =0; k<=j; k++){
            dp[i][j] = (dp[i][j] + dp[i-1][k])%10007;
        }
    }   
}
console.log(dp[input].reduce((r,v) => {return (r+v) % 10007} , 0))
```

### 14248 점프 점프

```jsx
const input = require("fs").readFileSync('/dev/stdin').toString().split('\n')

const bridge = Array.from({length: parseInt(input[0])}, (_, i) => i+1)
const start = parseInt(input[2])
const visited = []

const jumps = input[1].split(' ').map(v => parseInt(v))

const bfs = (pos) => {
    if(pos <= -1 || pos > bridge.length - 1 || visited.includes(pos)) {
       return;
    }
    visited.push(pos)
    bfs(pos - jumps[pos])
    bfs(pos + jumps[pos])
}

bfs(start - 1)

console.log(visited.length)
```

### 14912숫자빈도수

```jsx
var fs = require('fs')
var filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
var input = fs.readFileSync(filepath).toString().split(' ')

var N = parseInt(input[0])
var d = parseInt(input[1])

var arr= []
var cnt = 0

for(var i = 1; i <= N; i++){
    arr.push(i)
};
//일단 배열을 하나생성해서, push해줍니다.
let num = String(arr.join(''))
//일단 배열에 있는 숫자들을 문자열로 만들어줍니다.
let numArr = num.split('').map(n=>parseInt(n));
//그 후에 다시 split함수를 써서 각 숫자들로 쪼개줍니다.
for(let i = 0; i<num.length; i++){
    if(numArr[i]===d)
    cnt ++
}
//그리고 배열의 크기만큼 for문을 돌면서 그 숫자가 몇개들어있는지 세주면 됩니다.
console.log(cnt)
```

https://www.acmicpc.net/user/weihyuk39
<code>
#### 기수정렬

      from queue import Queue
      
      def radix_sort(A):
        queues = []
        for i in range(BUCKETS):
          queues.append(Queue()) #이거하는이유모르겠음 그냥 queues = Queue() 해주면 되는거아님?
          
        n = len(A)
        factor = 1 # 자릿 수
        for d in range(DIGITS) :
          for i in range(n):
            queues[ (A[i] // factor) % 10].put(A[i])
          j = 0                   #0은 뭐지 ?
          for b in range(BUCKETS):
            while not queues[b].empty():
              A[j] = queues[b].get()
              j += 1
          factor *= 10
          print("Step", d+1, A)
          
      import random
      BUCKETS = 10  #10개의 큐를 만들기 위한 공간
      DIGITS = 4    #네 자리수
      data = []     # data에 랜덤함수 넣어줘야함.
      for i in range(10):
        data.append(random.randint(1,9999))
      radix_sort(data)
      print("Radix: ", data)


#### Counting_sort
        - 이것도 고친 코드 오류남 
        
#### horspool알고리즘
     NO_OF_CHARS = 128

     def shift_table(pat):
          m = len(pat) #pat = BANANA #m은 6
          tbl = [m] * NO_OF_CHARS # tbl은 6이 128개 들어있는 배열

            for i in range(m-1):
                tbl[ord(pat[i])] = m - 1 - i  # 문자열을 아스키코드로 변환하는 함수  /// 배열의 자릿수를 따져야 하기때문에 -1을 해준다.
                #이렇게 해주는 이유를 모르겠음
            print('tbl string to askii', tbl)
            return tbl

        def search_horspool(T,P): #T = (APPLEMANGOBANANAGRAPE)text , P = (BANANA) pattern
            m = len(P)  #m은  6 패턴글자수
            n = len(T)  #n은   21 텍스트글자수
            t = shift_table(P)  #t는 P=BANANA
            i = m - 1  # i는 m을 인덱스화 시킨것
            while( i <= n - 1): #인덱스 비교 
                k = 0           #k = 0이 뭔데..
                while k <= m - 1 and P[m-1-k] == T[i-k]:
                                # 이거 거꾸로 비교
                                # k < m-1 은 
                    k+= 1

                if k == m:
                    # 만약 k랑 m이 같다면 

                    return i-m + 1
                else :
                    print('비교시작 문자 : ' ,T[i])
                    print('비교시작 문자의 이동표 값:' , t[ord(T[i])])
                    i+= t[ord(T[i])]
                    print("다음 비교할 위치 맨 끝 :",  i)


            return -1

        print("패턴의 위치 :", search_horspool("APPLEMANGOBANANAGRAPE", "BANANA"))

- 7
#### 이항계수
     def bino_coef_dp(n,k):
        C = [[-1 for _ in range(k+1)] for i in range(n+1)] #(2차원 테이블 : n은 열, k는 행) 5,3 하면
            # 속에 있는 배열이 6개니까 [-1,-1,-1,-1,-1,-1] *  60개 
        print(C)
        for i in range(n+1):
                # i는 0부터 60까지

            for j in range(min(i,k)+1):
                    #근까 왜 min을 써주는지 이해를 해야함 
                    # => 최대의 개수가 6임 그래서 넘어가면 
                    # i =  일때 , 
                    # for j in range(2)
                    # j = 0, 1, 2

                    if j == 0 or j == i:
                        C[i][j] = 1

                    else:
                        C[i][j] = C[i-1][j-1] + C[i-1][j]

        print("order : c", C)
        return C[n][k]

     print(bino_coef_dp(60,5))
       
#### 0-1 배낭 채우기 알고리즘(동적 계획법)


#### lcs
     def lcs_dp(X,Y):
        x_list = list(X)
        y_list = list(Y)
        m = len(x_list) # m == 11
        n = len(y_list) # n == 9

        L = [[None]*(n+1) for _ in range(m+1)]  # L = 9 * 11 

        for i in range(m+1):
            # i = 1,2,3,4,5,6,7,8,9,10,11,12 Hello world
          for j in range(n+1):
              # j = 0,1,2,3,4,5,6,7,8,9 game over
            if i == 0 or j == 0:
              L[i][j] =0

            elif X[i-1] == Y[j-1]:  
              L[i][j] = L[i-1][j-1] + 1
              # X[0] == 
            else:
              # 
              L[i][j] = max(L[i][j-1], L[i-1][j])
              print(L)
        return L[m][n]
      X = "hello world"
      Y = "game over"

      print(lcs_dp(X,Y))
      
#### Floyd 최단경로 탐색 알고리즘
      import copy

      def shortest_path_floyd(vertex, W):
        vsize = len(vertex)
        D = copy.deepcopy(W)
        # vsize == 6
        for k in range(vsize):     #경유지
          for i in range(vsize):   #출발지
            for j in range(vsize): # 도착지
                # k == 0  i == 1 // j == 2,3,4,5
              if(D[i][k] + D[k][j]< D[i][j]):   #D[i][k] + D[k][j]#k라는 노드를 거쳐가는 노드   // #D[i][j] 다이렉트
              # D[1][0] + D[0][2] < D[1][2]( B=>C)
                D[i][j] = D[i][k] + D[k][j]
          printD(D)

      def printD(D):
        vsize = len(D)
        print("============================================")
        for i in range(vsize):
            for j in range(vsize):
                if (D[i][j] == INF) : print(" INF ", end = "")
                else: print("%4d "%D[i][j], end= "")
            print("")

      INF = 9999
      vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
      weight = [[0,7,INF, INF, 3, 10, INF],
                [7,0,4,10,2,6,INF],
                [INF,4,0,2,INF,INF,INF],
                [INF, 10,2,0,11,9,4],
                [3, 2,INF,11,0,13,5],
                [10,6,INF,9,13,0,INF],
                [INF,INF,INF,4,5,INF,0]]
      shortest_path_floyd(vertex, weight)


########################


#### 편집 거리(동적 계획법, 메모제이션 사용)
        - 11.22 알고리즘 코드 오류 남 달라고 하기
        
#### 동전 거스름돈(greedy)
           def min_coins_greedy(coins,V):
            data = []
            for coin in coins:
                res = V // coin 
                data.append(res)
                V = V - coin * res
            return data

        coins = [500,100,50,10,5,1]
        V = 580

print("잔돈 액수 = ", V)
print("동전 종류 = ", coins)
print("동전 갯수 = ", min_coins_greedy(coins,V))
 
 
     
     
     
#### 동전 거스름돈 (다이나믹 프로그래밍으로 풀기)
     -  



#### 분할 가능한 배낭 채우기( 탐욕적 기법)
     
        # def f ( o ):
        #     return o[2]/o[1]
        #     === 
        #     lambda o: o[2]/o[1]

        def KnapSack_fractional_greedy(obj,W):
            obj.sort(key = lambda o:o[2]/o[1], reverse = True)
        # lambda 인자 : 표현식
            print(obj)
        # sort=>[('B', 12, 120), ('A', 10, 80), ('C', 8, 60)]
            totalValue = 0
            for o in obj :
                ## o == ('A', 10, 80)
                if W <= 0 : break


                if W - o[1] >= 0:

                    W -= o[1]
                    ## W == 6
                    totalValue += o[2]
                    ## totalValue = 120
                else:
                    fraction = W / o[1]
                    ## fraction = 6 / 10 ==> 0.6
                    totalValue += o[2] * fraction
                    ## totalValue = 120 + 48
                    W = int(W-(o[1] * fraction))
                    ## W = 0
            return totalValue
        obj = [("A",10,80), ("B",12,120), ("C",8,60)]
        #A는 10kg당 80억// B는 12kg당 120억// C는 8kg당 60억

        print("W=18",obj)
        print("부분적인 배낭", KnapSack_fractional_greedy(obj,18)) 

#### 최소비용 신장트리 Prim
</

#### 최소비용 신장트리 Kruskal

#### Dijkstra의 최단경로 알고리즘

#### 허프만 트리 생성 알고리즘

