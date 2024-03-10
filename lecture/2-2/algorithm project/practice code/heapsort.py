def heapify_down(A, k, n): #작은 값을 아래로

    while 2*k+1 < n:  #자식노드가 있는가?
        L,R = 2*k+1,2*k+2            #L 왼쪽 자식노드, 우측 자식노드
        if (L<n) and (A[L] > A[k]): #부모노드와 비교
            m=L
        else:
            m=k
        if R<n and A[R]> A[m]:
            m=R
        if m!=k: #m = max 아니면 교환
            A[k], A[m] = A[m],A[k]
            k=m
        else: break

def heap_sort(A):
    n=len(A)
    for k in range(n-1,-1,-1):
        heapify_down(A,k,n)
    for k in range(len(A)-1,-1,-1):
        A[0],A[k]=A[k],A[0]
        n=n-1
        heapify_down(A,0,n) 

    return A

A=[6,5,4,37,8,1,34,13,631,72,345,143,1324,3,2436,3,1324,125,3123,412,35,324,6,23,62,436]
print(heap_sort(A))