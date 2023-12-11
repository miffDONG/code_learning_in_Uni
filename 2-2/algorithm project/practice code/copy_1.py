def print_subset(x):
    print([A[i] for i in range(len(x)) if x[i]])

def subset_sum(k):
    for i in range(0,k):
        if A[i] == 1:
	        v_sum += A[i]
            
    if k == len(A) and v_sum == S:
        print_subset(x)
    else:
        if v_sum + A[k] <= S:
            x[k] = 1
            subset_sum(k+1)
        else:
            x[k] = 0
            subset_sum(k+1)
				
        # code for x[k] = 1 and x[k] = 0

A = list(set(int(x) for x in input().split()))
A.sort()
S = int(input()) 
x = [0]*len(A)
subset_sum(0)