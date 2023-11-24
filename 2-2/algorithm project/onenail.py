
# n=int(input())
# f=[0]*n
# l=[0]*n

# for i in range(0,n):
#     f[i],l[i]=map(int,input().split())

n=int(input())
f=[0]*n
l=[0]*n
for i in range(0,n):
    f,l=map(int,input().split())

print(f)
print(l)
f.sort()
l.sort()

print(f)
print(l)
answer=0
index=[]
i=0
#시작점을 오름차순으로 정렬한 list f[0]an only concatenate tuple (not "int") to tuple~f[last] 범위를 k로 지정 하나씩 
# for k in range(f[0],f[len(f)-1]+1):
# for k in f:
# for k in range(list[0][0],list[len(list)-1][0]+1):
#     if i<n and list[i][0]==k:
#         index.append(i)
#         i+=1
#     while i<n and list[i-1][0]==list[i][0]: #중복값이 있는경우 상수시간 
#         index.append(i)
#         i+=1
    
#     removeIndex=[]
#     for j in range(0,len(index)):
#         if list[index[j]][1]+1==k: 
#             removeIndex.append(j)
#     o=0
#     if len(removeIndex)>0:
#         for m in removeIndex:
#             index.pop(m-o)
#             o+=1

#     answer=max(answer,len(index))
     
# print(answer)
print(list)
for t in range(0,n):
    k=list[t][0]
    index.append(i)
    i+=1
    
    # removeIndex=[]
    o=0
    for j in range(0,len(index)):
        if list[index[j]][1]+1<=k: 
            index.pop(j-o)
            o+=1

    # for j in range(0,len(index)): #최악의 경우는 모든 막대기의 끝이 마지막 막대기의 시작점을 지나가는 경우 #O(n)
    #     if list[index[j]][1]+1==k: 
    #         removeIndex.append(j)
    # o=0
    # if len(removeIndex)>0:
    #     for m in removeIndex:
    #         index.pop(m-o)
    #         o+=1


    answer=max(answer,len(list))
     
print(answer)

for k in range(list[0][0],list[len(list)-1][0]+1):
    if i<n and list[i][0]==k:
        index.append(i)
        i+=1
    while i<n and list[i-1][0]==list[i][0]: #중복값이 있는경우  상수시간O(1)
        index.append(i)
        i+=1
    
    removeIndex=[] #막대기의 마지막점이 범위 안의 특정 지점에서 벗어나면 삭제
    for j in range(0,len(index)): #최악의 경우는 모든 막대기의 끝이 마지막 막대기의 시작점을 지나가는 경우 #O(n)
        if list[index[j]][1]+1==k: 
            removeIndex.append(j)
    o=0
    if len(removeIndex)>0:
        for m in removeIndex:
            index.pop(m-o)
            o+=1

    answer=max(answer,len(index))
     
print(answer)