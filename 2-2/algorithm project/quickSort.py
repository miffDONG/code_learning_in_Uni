def quick_sort(A,first,last):
    if first >= last: return
    print(A)
    p=A[first]
    left=first+1
    right=last
    while left<=right:
        while left<=last and A[left]<p:
            left+=1
        while right>first and A[right]>p:
            right-=1
        if left<=right:
            A[left],A[right]=A[right],A[left]
            left+=1
            right-=1

    A[first],A[right]=A[right],A[first]

    quick_sort(A,first,right-1)
    quick_sort(A,right+1,last)

    
A=[4,5,1,3,10,4,7,1]
print(quick_sort(A,0,len(A)-1))
print(A)