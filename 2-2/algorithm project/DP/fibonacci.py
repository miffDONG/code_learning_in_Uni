
# # 1 1 2 3 5 8 13
# #재귀 알고리즘
# def fibo1(n):
#     if n<=1: return n
#     return fibo(n-1) + fibo(n-2)

# print(fibo1())

# #문제점 : 중복 계산


#######################################################

#코드 못 짰는데 나한테 재귀는 너무 어려워 \
#기록 + 재사용 재귀 알고리즘


###이게
memo = [0]

def fibo(n):    
    global memo    

    #memo의 길이가 4면 0~3번째까지 값이 저장돼있음.
    if n<=len(memo):
        return memo[n]

    if n <= 1:
        f = n

    else: 
        f = fibo(n-1) + fibo(n-2)

    memo.append(f)
    return f


    
print(fibo(5))

# # 기록 + 재사용 비재귀 알고리즘 
# # 배열에다가 넣으면서 중복되면 
# def fibo(n):
#     F = [0,1]
#     for k in range(2,n+1):
#         F.append(F[k-1]+F[k-2])
#     return F[n]

# print(fibo(5))