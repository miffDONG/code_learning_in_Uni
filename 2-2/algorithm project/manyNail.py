# def quick_sort(f,l,first,last):
#     if first >= last: return
#     p=l[first]
#     left=first+1
#     right=last
#     while left<=right:
#         while left<=last and l[left]<p:
#             left+=1
#         while right>first and l[right]>p:
#             right-=1
#         if left<=right:
#             f[left],f[right]=f[right],f[left]
#             l[left],l[right]=l[right],l[left]
#             left+=1
#             right-=1


#     f[first],f[right]=f[right],f[first]
#     l[first],l[right]=l[right],l[first]

#     quick_sort(f,l,first,right-1)
#     quick_sort(f,l,right+1,last)


def insertion_sort(f,l,first,last):
    i=first
    k=last
    while i<k:
        i+=1
        j=i-1
        while j>=0 and f[j]>f[j+1]:
            f[j],f[j+1]=f[j+1],f[j]
            l[j],l[j+1]=l[j+1],l[j]
            j=j-1
    return f,l


n=int(input())
list=[0]*n

for i in range(0,n):
    list[i]=tuple(map(int,input().split()))



list.sort(key=lambda x:x[1])
print(list)
index=[]
nail=[list[0][1]] #마지막점만 넣을거임.
ni=0 #nail index
for k in range(1,n):
    if list[k][0]<=nail[ni] and list[k][1]>=nail[ni]:
        pass
    elif list[k][1]>nail[ni]:
        nail.append(list[k][1])
        ni+=1
print(len(nail))