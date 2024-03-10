import random, timeit

##
## 여기에 세 가지 정렬함수를 위한 코드를...
##
def quick_sort(A,first,last):
    if first >= last: return
    global Qs
    global Qc
    p=A[first]
    left=first+1
    right=last
    while left<=right:
        while left<=last and A[left]<p:
            left+=1
            Qc+=1
        while right>first and A[right]>p:
            right-=1
            Qc+=1
        if left<=right:
            A[left],A[right]=A[right],A[left]
            left+=1
            right-=1
            Qs+=1


    A[first],A[right]=A[right],A[first]
    Qs+=1

    quick_sort(A,first,right-1)
    quick_sort(A,right+1,last)


def merge(A,first,last):
	m=(first+last)//2
	i,j=first,m+1
	B=[]

	global Mc
	global Ms
	while i <= m and j <= last:
		if A[i]<=A[j]:
			B.append(A[i])
			i+=1
			Mc+=1
			Ms+=1
		else:
			B.append(A[j])
			j+=1
			Mc+=1
			Ms+=1


	# while i<=m:
	for k in range(i,m+1):
		B.append(A[i])
		i+=1
		Ms+=1

	# while j<=last:
	for k in range(j,last+1):
		B.append(A[j])
		j+=1
		Ms+=1
		
	for i in range(first,last+1): #범위 range(,A-1 주의)
		A[i] = B[i-first]
		Ms+=1

def merge_sort(A,first,last):
	if first >= last: 
		return
    
	m = (first + last)//2
	merge_sort(A,first,m)
	merge_sort(A,m+1,last)
	merge(A,first,last)
# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#
def heapify_down(A, k, n): #작은 값을 아래로
    global Hc
    global Hs
    while 2*k+1 < n:  #자식노드가 있는가?
        L,R = 2*k+1,2*k+2            #L 왼쪽 자식노드, 우측 자식노드
        if (L<n) and (A[L] > A[k]): #부모노드와 비교
            m=L
            Hc+=1
        else:
            m=k
            Hc+=1
        if R<n and A[R]> A[m]:
            m=R
            Hc+=1  #우측 좌측 자식노드를 부모노드와 비교 끝
        if m!=k: #m = max 아니면 교환
            A[k], A[m] = A[m],A[k]
            k=m
            Hs+=1
        else: break

def heap_sort(A):
    n=len(A)
    global Hs
    for k in range(n-1,-1,-1):
        heapify_down(A,k,n)
    for k in range(len(A)-1,-1,-1):
        A[0],A[k]=A[k],A[0]
        Hs+=1
        n=n-1
        heapify_down(A,0,n) 

    return A

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:]
C = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))

print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))


# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))