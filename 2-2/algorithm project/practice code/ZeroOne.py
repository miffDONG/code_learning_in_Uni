k=int(input()) #배낭크기
n=int(input()) #아이템 개수
size_of_n=list(map(int,input().split()))
value_of_n=list(map(int,input().split()))

#가성비 계산 O(n)
sv=[]
for i in range(0,n):
    sv.append([])
    sv[i].append(value_of_n[i]/size_of_n[i])
    sv[i].append(i)
#가성비 내림차순 정렬O(nlogn)
sv.sort(key=lambda x:-x[0])


#MaxProfit 정하기
#fractional MaxProfit = 
MaxProfit=0
M_size=0
Mi=0
while (M_size+size_of_n[sv[Mi][1]])<k:
    MaxProfit+=value_of_n[sv[Mi][1]]
    M_size+=size_of_n[sv[Mi][1]]
    Mi+=1
MaxProfit=MaxProfit+(value_of_n[sv[Mi][1]]/size_of_n[sv[Mi][1]]*(k-M_size))

#사이즈별 가치 
#선택된 애들 다 더하고, 그 뒤 애들로 값 계산
#b값 = 예상최대이익
#i 이후의 값들을 계산해야함.
#n보다 작을때 사이즈가 괜찮다면 계속해서 더하고 마지막에 단위당크기로 계산

def fractional(i,size):
    f_p,f_s=0,0
    if i==n or size <=0:
        return 0
    j=i
    f_size=size
    #i뒤로 사이즈가 조건에 맞으면 계속해서 더함.
    while j<n and size_of_n[sv[j][1]] <= f_size:
        f_p+=value_of_n[sv[j][1]]
        f_s+=size_of_n[sv[j][1]]
        f_size-=size_of_n[sv[j][1]]
        j+=1
    #잔여 사이즈로 마지막 물건 잘라서 넣기
    if j<n and f_size>0:
        f_p+=value_of_n[sv[j][1]]/size_of_n[sv[j][1]]*(f_size)

    return f_p

mp=0 # 가장 좋은 선택에 대한 가격의 합
x=[0]*n #뽑기 리스트 선택 1, 선택x 0
def knapsack(i,size):
    p,s=0,0
    global mp
    if i==n or size <=0:
        # print(x)
        return

    for j in range(0,i):
        if x[sv[j][1]]==1: 
            p+=value_of_n[sv[j][1]] #가치 합
    for j in range(0,i):
        if x[sv[j][1]]==1: 
            s+=size_of_n[sv[j][1]] #크기 합
  
    if size_of_n[sv[i][1]] <= size:
        b=fractional(i+1,size-size_of_n[sv[i][1]])
        if (p+value_of_n[sv[i][1]]+b)>mp:
            if (p+value_of_n[sv[i][1]])>mp:
                mp = p + value_of_n[sv[i][1]] 
                x[sv[i][1]] = 1
                knapsack(i+1, size-size_of_n[sv[i][1]])
    
    b=fractional(i+1,size)
    if p+b>mp:
        x[sv[i][1]]=0
        knapsack(i+1, size)

        #뭐가 문제야 ?????????

knapsack(0, k)
print(mp)