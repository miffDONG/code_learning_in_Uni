def insertion_sort(A,first,last):
    i=first
    k=last
    while i<k:
        i+=1
        j=i-1
        while j>=0 and A[j]>A[j+1]:
            A[j],A[j+1]=A[j+1],A[j]
            j=j-1
    return A

A=[1,1234,123,512,34,2,34,2,34,123,5,123,4,1235,4,34,6,45,34,56,345]

print(insertion_sort(A, 0, len(A)-1))