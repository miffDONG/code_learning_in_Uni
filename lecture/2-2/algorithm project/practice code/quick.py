# a=[]
# for i in range(6):
#     if i%3: a.append(2*i)
#     else: a.append(2*i-1)

# print(a)
# a.pop()
# a.pop(0)
# a.insert(2,9)
# print(a)

# def f(n):
#     c=0
    
#     for i in range(1,n):
#         j=1
#         while j<n:
#             c+=1
#             j*=2
#     return c

# print(f(6))

# A=[1,2,3,4,5]
# print(A[-1])

def quickSort(A):
    if len(A)<=1:return A
    print(A)
    S,M,L =[],[],[]
    p=A[0]
    for a in range(0,len(A)):
        if A[a]<p:S.append(A[a])
        elif A[a]==p:M.append(A[a])
        else: L.append(A[a])
    return quickSort(L) + M + quickSort(S)

A = quickSort([4,5,1,3,10,4,7,1])


# A=[0,1,2,3,4,5,6,7,8]
# for i in range(0,len(A)):
#     print(A[i])