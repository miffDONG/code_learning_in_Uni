import random, timeit

# def quick_sort1(A,first,last):
#     if first >= last: return 
#     global Qs
#     global Qc
#     p=A[first]
#     left=first+1
#     right=last
#     while left<=right:
#         while left<=last and A[left]<p:
#             left+=1
#             Qc+=1
#         while right>first and A[right]>p:
#             right-=1
#             Qc+=1
#         if left<=right:
#             A[left],A[right]=A[right],A[left]
#             left+=1
#             right-=1
#             Q1s=1


#     A[first],A[right]=A[right],A[first]
#     Qs+=1

#     quick_sort1(A,first,right-1)
#     quick_sort1(A,right+1,last)

def quick_insertion2(A,first,last):
    if first+30 >= last: 
        return
    global Ps
    global Pc
    p=A[first]
    left=first+1
    right=last
    while left<=right:
        while left<=last and A[left]<p:
            left+=1
            Pc+=1
        while right>first and A[right]>p:
            right-=1
            Pc+=1
        if left<=right:
            A[left],A[right]=A[right],A[left]
            left+=1
            right-=1
            Ps+=1


    A[first],A[right]=A[right],A[first]
    Ps+=1

    quick_insertion2(A,first,right-1)
    quick_insertion2(A,right+1,last)

    if last-first+1==len(A):
        insertion_sort2(A,first,last)

def quick_insertion1(A,first,last):
    if first+30 >= last: 
        insertion_sort1(A,first,last)
        return
    global Is
    global Ic
    p=A[first]
    left=first+1
    right=last
    while left<=right:
        while left<=last and A[left]<p:
            left+=1
            Ic+=1
        while right>first and A[right]>p:
            right-=1
            Ic+=1
        if left<=right:
            A[left],A[right]=A[right],A[left]
            left+=1
            right-=1
            Is+=1


    A[first],A[right]=A[right],A[first]
    Is+=1

    quick_insertion1(A,first,right-1)
    quick_insertion1(A,right+1,last)



def insertion_sort1(A,first,last):
    global Ic
    global Is
    i=first
    k=last
    while i<k:
        i+=1
        j=i-1
        while j>=0 and A[j]>A[j+1]:
            A[j],A[j+1]=A[j+1],A[j]
            j=j-1
            Ic+=1
            Is+=1


def insertion_sort2(A,first,last):
    global Pc
    global Ps
    i=first
    k=last
    while i<k:
        i+=1
        j=i-1
        while j>=0 and A[j]>A[j+1]:
            A[j],A[j+1]=A[j+1],A[j]
            j=j-1
            Pc+=1
            Ps+=1


def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

Qc, Qs, Ic, Is = 0, 0, 0, 0
Lc,Ls=0,0
Pc,Ps=0,0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:]
C = A[:]


# # print(B)
print("Quick insertion1:")
print("time =", timeit.timeit("quick_insertion1(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Ic, Is))

print("")
print("Quick insertion2:")
print("time =", timeit.timeit("quick_insertion2(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Pc, Ps))

# print("Insertion sort:")
# print("time =", timeit.timeit("insertion_sort(C, n)", globals=globals(), number=1))
# print("  comparisons = {:10d}, swaps = {:10d}\n".format(Lc, Ls))
# print(B)
assert(check_sorted(A))
assert(check_sorted(B))
# assert(check_sorted(C))
