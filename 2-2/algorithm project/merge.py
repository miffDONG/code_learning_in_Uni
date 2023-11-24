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



A=[4,2,5,8,6,2,3,7,10]
print(merge_sort(A,0,len(A)-1))
print(A)