# def MoM(MoM_list,k):
#     if len(MoM_list) == 1:
#         return MoM_list[0]
#     S,L,M,medians=[],[],[],[]
#     n = len(MoM_list)
    
    
#     for i in range(n):
#         m=n//2
#         medians.append(MoM_list[i][m])

# def MoM_true(exist_list,k):
    # if len(exist_list) ==1:
    #     if exist_list[0] == k: return True
    #     else: return False

#     A,M,B,medians = [],[],[],[]
#     n=len(exist_list)
#     i=0 
#     while i+4<n:
#         medians.append(find_median_five(A[i:i+5])) 
#         i+=5

#     if i<n and i+4>=n:
        

#     mom = MoM(medians,int(len(medians)//2))
#     ## A,B영역 나누기
#     for v in A: 
#         if v<mom:A.append(v)
#         elif v>mom:B.append(v)
#         else:M.append(v)
#     #k값 위치 찾기
#     if mom<k: return MoM_true(A,k)
#     elif mom>k: return MoM_true(B,k)
#     else : return true

# def find_median_five(A):
#     n=len(A)
#     median = 0
#     win1,win2,lose1,lose2=0,0,0,0
#     a,b=0,0

#     if A[0]>A[1]: 
#         win1=A[0]
#         lose1=A[1]
#     else: 
#         win1=A[1]
#         lose1=A[0]
#     if A[2]>A[3]: 
#         win2=A[2]
#         lose2=A[3]
#     else: 
#         win2=A[3]
#         lose2=A[2]

#     if win1>win2: a=win2
#     else: a=win1
#     if lose1>lose2: b=lose1
#     else: b=lose2
#     c=A[4]


#     if(b>=a and c<=a) or (b<=a and c>=a): return a
#     elif(b>=c and b<=a) or (b>=a and b<=c): return b
#     else: return c

        


    # print(MoM_list)
    # print(len(MoM_list[1]))
    # print(len(MoM_list[1])//2)
    # print(len(MoM_list))
    # print(medians)


n,k=input().split()
n=int(n)
k=int(k)
MoM_list=[]
exist_list=[]
for i in range(n):
    MoM_list.append(list(map(int, input().split())))

print(MoM_list)
# exist_list=[4,2,1,3,0,8,6,7,5,9,11,10,14,13,12,15]
# for i in range(n):
#     for k in range(n):
#         exist_list.append(MoM_list[i][k])

# print(exist_list)


# MoM(MoM_list,k)

# MoM_k_true(exist_list, 8)
# A=[1,2,4,5,3]
# print(find_median_five(A))