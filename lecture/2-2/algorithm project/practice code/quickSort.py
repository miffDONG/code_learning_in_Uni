# def quick_sort(A,first,last):
#     if first >= last: return
#     print(A)
#     p=A[first]
#     left=first+1
#     right=last
#     while left<=right:
#         while left<=last and A[left]<p:
#             left+=1
#         while right>first and A[right]>p:
#             right-=1
#         if left<=right:
#             A[left],A[right]=A[right],A[left]
#             left+=1
#             right-=1

#     A[first],A[right]=A[right],A[first]

#     quick_sort(A,first,right-1)
#     quick_sort(A,right+1,last)

    
# A=[4,5,1,3,10,4,7,1]
# print(quick_sort(A,0,len(A)-1))
# print(A)

def quick_sort(A,first,last):
   Qc,Qs=0,0
   if first>=last:
      return Qc,Qs
   left,right=first+1,last
   pivot=A[first]
   while left<=right:
      while left<=last and A[left]<pivot:
         left+=1
         Qc+=1
      while right>first and A[right]>pivot:
         right-=1
         Qc+=1
      if left<=right:
        A[left],A[right]=A[right],A[left]
        Qs+=1
        left+=1
        right-=1
   
   #move pivot      
   A[first],A[right]=A[right],A[first]
   Qs+=1
   
   quick_sort(A,first,right-1)
   quick_sort(A,right+1,last)

   return Qc,Qs

A=[4,5,1,3,10,4,7,1]
print(quick_sort(A,0,len(A)-1))
print(A)