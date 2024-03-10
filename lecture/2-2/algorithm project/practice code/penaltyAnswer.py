W = int(input())
words = input().split()
# code below
#단어들의 길이를 저장한 리스트
lengths = [len(x) for x in words] 
print(lengths)
#단어들의 길이 합을 저장한 리스트 -> 단어가 한 줄에 나올 때, 길이 구하기가 수월함
#i가 0일때의 조건을 따로 주지 않기 위해 앞에 0을 하나 붙여준다.
prefix = [0]*(len(words)+1)
print(prefix)
prefix[1] = lengths[0]
print(prefix)
for i in range(2,len(words)+1):
   prefix[i] = prefix[i-1]+lengths[i-1]
print(prefix)
#penalty[i][j] = i번째 단어에서 j번째 단어까지 왼쪽 맞춤할 때, 최소 penalty   
#문장 12345를 왼쪽 맞춤한다고 가정하면
#최소 penalty는 
#1왼쪽 맞춤 + 2345왼쪽 맞춤, 12왼쪽 맞춤+345왼쪽 맞춤,.....,1234왼쪽 맞춤 + 5왼쪽 맞춤, 12345왼쪽 맞춤 중의 하나이다.
#그래서 penalty[i][j]= min(penalty[i][i] + penalty[i+1][j],...,penalty[i][j-1] + penalty[j][j])
#그런데 12345왼쪽 맞춤의 경우 한 문장이 한 줄에 들어가는 경우이다.
#미리 구해놓았던 prefix리스트를 이용하여 문장의 길이와 공백의 길이를 W에서 빼준 값이 0보다 같거나 크면 
#그 값또한 penalty[i][j]를 구하기 위한 후보로 넣어준다. 
penalty = [
   [0]*len(words)
   for _ in range(len(words))
]
print(penalty)
#i번째부터 i번째까지 -> 한 줄에 i번째 단어 하나만 있는 경우
for i in range(len(words)):
   penalty[i][i] = (W-lengths[i])**3
print(penalty)
#i번째부터 j번째까지 반복문을 통해 penalty 값 저장
#구하고 싶은 penalty값은 0인덱스부터 len(words)인덱스까지이므로 아래에서부터 채워준다.
#penalty[i][j]값을 구하려면 왼쪽 값과, 아래 값들이 필요하기 때문에 밑에서부터 오른쪽으로 진행하였다.
for i in range(len(words)-2,-1,-1):
   for j in range(i+1,len(words)):
      #penalty[i][i]에서 penalty[i][j-1]까지 진행
      af, al = i, i #옆으로 이동
      #penalty[i+1][j]에서 penalty[j][j]까지 진행
      bf, bl = i+1, j #밑으로 이동
      #penalty의 초기값으로 penalty[i][i] + penalty[i+1][j]으로 지정
      penalty[i][j] = penalty[af][al]+penalty[bf][bl]
      while al < j:
         #i부터 j까지 단어가 한 줄에 있을 경우 길이
         score = prefix[j+1] - prefix[i] + (j-i)
         #초기에 설정해준 폭인 W보다 문장 길이가 작거나 같으면 실행
         if score <= W:
            #현재 penalty값과 한 문장에 있을 경우의 penalty값중 최소값 저장
            penalty[i][j] = min((W-score)**3,penalty[i][j])
         #현재 penalty값과 다른 조합에서의 penalty 합 중 최소값 저장
         penalty[i][j] = min(penalty[i][j],penalty[af][al]+penalty[bf][bl])
         #모든 경우를 탐색하기 위해 al는 오른쪽으로, bf는 밑으로 이동
         al+=1 
         bf+=1

#0인덱스부터 len(words)-1인덱스까지 왼쪽 맞춤한 최소 penalty값 출력
print(penalty[0][len(words)-1])

'''
수행시간 분석
9번째 줄의 for문에서 단어의 개수인 n-1만큼 진행 -> O(n)
26번째 줄의 for문에서 단어의 개수인 n만큼 진행 -> O(n)
32번째 줄부터의 중첩된 반복문은 
총 개수를 세면 마지막 부터 1 + (1+2) + (1+2+3) + (1+2+3+4) +.....+n(n-1)/2 
이를 풀면 1이 n-1개, 2가 n-2개,........,n-1이 1개이다.
i=1부터 i=n-1까지 i(n-i)를 진행하면 된다.
풀면, i=1부터 i=n-1까지 in, i=1부터 i=n-1까지 i^2
정리하면 n*n(n-1)/2 + i=1부터 i=n-1까지 i^2인데, i<n이므로 i^2 < ni이다. 
즉, in에서 n^3이 나오고 i^2에선  n^3보다 작은 값이 나온다.
이것을 Big-O로 표현하면 O(n^3)이 된다.
'''