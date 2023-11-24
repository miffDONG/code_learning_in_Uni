def fibo(n):
	k=0
	F=0
	H=0
	L=1
	while n > k:
		F=H
		H=L
		L=F+L
		k=k+1
	return L

n=int(input())
print(fibo(n))