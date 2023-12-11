
n=int(input())
f=[0]*n
l=[0]*n
for i in range(0,n):
    f[i],l[i]=map(int,input().split())

f.sort()
l.sort()
f_i=0
l_i=0
number=0
answer=0
#시작점을 오름차순으로 정렬한 list f[0]an only concatenate tuple (not "int") to tuple~f[last] 범위를 k로 지정 하나씩 
for k in range(f[0],f[len(f)-1]+1):
    while f_i<n and k==f[f_i]:
        number+=1
        f_i+=1

    while l_i<n and k==l[l_i]+1:
        number-=1
        l_i+=1

    answer=max(answer,number)
     
print(answer)
