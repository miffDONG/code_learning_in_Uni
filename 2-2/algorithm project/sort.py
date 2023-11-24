#코드 가져다가 쓰고 중점은 데이터 수집 및 논리설명
#quick 
#추가점수 원래는 아래가 1개가 될때까지 쪼개야하는데 
#예) 10개까지만 쪼개고 insertion sort 하고 비교
#예2) 중간까지 내려가고 올라 온 후 insertion sort
#merge
#heap

#1.비교횟수
#2.이동횟수(교체횟수)
#3.실행시간

def insertion_sort(A,n):
	for i in range(1,n):
		j=i-1
		while j>=0 and A[j]>A[j-1]:
			A[j],A[j-1] = A[j-1],A[j]
			j=j-1

def selection_sort(A,n):
	for i in range(n-1,0,-1):
		m=max_index(A,i)
		A[i],A[m] = A[m]=A[i]

def Bubble_sort(A,n):
	for i in range(n):
		for j in range(1,n):

def merge(A,first,last):
	m=(first+last)//2
	i,j=first,m+1
	B=[]

	while i <=m and j <=last:
		if A[i]<A[j]:
			B.append(A[i])
			i+=1
		else:
			B.append(A[j])
			j+=1

	for 

def merge_sort(A,first,last):
	if first >= last: return
	m = (first + last)//2
	mergeSort(A,first,m)
	mergeSort(A,m+1,last)
	merge(A,first,last)

	
	
	
	
	
	
	