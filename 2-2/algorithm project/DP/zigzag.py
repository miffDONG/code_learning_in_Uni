A=[1,7,4,9,2,5]

n=len(A)
low=[0]*n
high=[0]*n

def zig(k):
    if k == n:
        return max(low[k-1],high[k-1])

    for i in range(1,k):
        if A[i-1]<A[i]:
            high[k]= low[k-1]+1
    high[k] = [(low[k-1]+1) for i in range(k) if A[k-1]<A[k]]
    low[k] = [(high[k-1]+1) for i in range(k) if A[k-1]>A[k]]

    return zig(k+1)

print(zig(1))