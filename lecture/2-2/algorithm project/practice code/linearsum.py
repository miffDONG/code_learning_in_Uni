def solve(list,L,S,k): #L=길이 , S=입력된 자릿수 합, K=현재 자릿수 합 #1~S까지 차례로 올라갈 값 list는 계속 넘겨줄거임
    l1=[] #모든 경우의 수
    se=L
    a=se
    # l2=[] #중복값 제거한 경우의 수
    if k>1 and k==S:
        return len(list)
    if k == 1:
        list.append(10**(L-1))
        if k==S: return len(list)            
    for i in list:
        for j in range(0,a): # 자릿수만큼의 반복 횟수
            if (i+10**j) not in l1:
                l1.append(i+10**j)
            elif a==0 and (i+1 not in l1):
                li.append(i+1)
        
        if a==0 and se>0:
            se-=1
            a=se
        elif k>2 and a!=0:
            a-=1

    # for value in l1:
    #     if value not in l2:
    #         l2.append(value)

    return solve(l1, L, S, k+1)


#0부터S까지 숫자가 올라갈 예정
k=1
L=5
S=5


list=[]
len=solve(list, L, S, k)
print(len)

# def solve(list,L,S,k): #L=길이 , S=입력된 자릿수 합, K=현재 자릿수 합 #1~S까지 차례로 올라갈 값 list는 계속 넘겨줄거임
#     l1=[] #모든 경우의 수
#     # l2=[] #중복값 제거한 경우의 수
#     ci=L
#     if k>1 and k==S:
#         return len(list)
#     if k == 1:
#         list.append(10**(L-1))
#         if k==S: return len(list)            
#     for i in list:
#         for j in range(0,L): # 자릿수만큼의 반복 횟수
#             if (i+10**j) not in l1:
#                 l1.append(i+10**j)

#     return solve(l1, L, S, k+1)
