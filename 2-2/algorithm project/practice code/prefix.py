import time, random

def prefixSum1(X, n):
	# S=[]
	# S[0]=X[0]
	# for i in range(1,n-1):
	# 	S[i]=S[i-1]
	# 	for j in range(0,n-1):
	# 		S[i]+=X[j]	
    for i in range(0,n-1):
        S[i]=0
		for j in range(0,n-1):
			S[i]+=X[j]
				
def prefixSum2(X, n):
	# code for prefixSum2
	
random.seed()		# random 함수 초기화
n=int(input()) # n 입력받음
N=[]
for i in range(0,n-1):
	number=random.randint(1,10000)
	# 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움
# prefixSum1 호출
# prefixSum2 호출
# 두 함수의 수행시간 출력