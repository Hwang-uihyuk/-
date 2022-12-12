# Baekjoon


https://www.acmicpc.net/user/weihyuk39
<code>
#### 기수정렬

      from queue from Queue
      
      def radix_sort(A):
        queues = []
        for i in range(BUCKETS):
          queues.append(Queue()) #이거하는이유모르겠음 그냥 queues = Queue() 해주면 되는거아님?
          
        n = len(A)
        factor = 1 # 자릿 수
        for d in range(DIGITS) :
          for i in range(n):
            queues[ (A(i) // factor) % 10].put(A[i])
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
</code>
