def make_number(words): #문장 -> 숫자로 변환
    n=len(words)
    number = 0
    list=[]
    for i in range(0,n):
        list.append(len(words[i]))
    return list


def divide(numberA,W):    # W크기만큼 문자열들 모으기
    n=len(numberA)
    space=1     # 띄어쓰기 공백 1
    S=[]        # 합
    I=[]        # 띄어쓰기에 None으로 구간 나눔.
    Noneindex=[]
    i=1
    j=0
    noneNum=0
    S.append(numberA[0])
    I.append(0)
    
    while i<n:
        if j>(len(S)-1):
            S.append(numberA[i])
            I.append(i)
            i+=1
        if S[j]<W-1 and i<n:    # 다음 숫자와 더할 수 있는 최솟 값 (w-2) ex) if w=8: 6 + 1(space) + 1(or S[j]<W-1)
            if S[j] + numberA[i] + space <= W:
                if j>len(S)-1:
                    S.append(numberA[i])
                    I.append(i)
                    i+=1
                else:
                    S[j] = S[j] + numberA[i] + space
                    I.append(i)
                    i+=1
            else: 
                j+=1
                I.append(None)
                Noneindex.append(len(I)-1)
        else:
            j+=1
            I.append(None)
            Noneindex.append(len(I)-1)
    Noneindex.pop()
    I.pop()
    return S,I,Noneindex

    ####################################################################################
    ##### 앞으로 S를 최대한 밀어넣었는데, None 앞 값을 뒤로 한번씩 밀으면서 3제곱 값을 구하고
    # 작은 값은 MIN에 계속 초기화/

def penalty(numberA,S,I,Noneindex,W,min):
    l=len(I)
    space=1
    remember=[]
    NoneCount=len(Noneindex)-1
    SS=[]
    for i in S:
        SS.append(i) # 변화가 없으면 더 이상의 경우의 수는 없으므로 확인하기 위한 데이터

    #마지막 그룹에 하나 더하고 앞에 원소에서 모든 원소의 이동 및 계산 실행. 반복. 첫번째 그룹까지 가면 모든 경우 계산 완료
    for i in range(len(S)-1,-1,-1):
        if S[NoneCount]+numberA[I[Noneindex[NoneCount-1]-1]]+space<=30:
            S[NoneCount-1] = S[NoneCount-1]-space-numberA[I[Noneindex[NoneCount-1]-1]]
            S[NoneCount] = S[NoneCount] + space + numberA[I[Noneindex[NoneCount-1]-1]]
            I[Noneindex[NoneCount-1]-1],I[Noneindex[NoneCount-1]]=I[Noneindex[NoneCount-1]],I[Noneindex[NoneCount-1]-1]
            Noneindex[NoneCount]-=1
            NoneCount-=1
            an=ans(S,W)
            if an<min:
                min=an
            break
        else: 
            NoneCount-=1


    #탈출조건 / 더 이상의 경우의 수는 없음.
    if SS==S:
        return min
    else: 
        SS[NoneCount+1]=S[NoneCount+1]
        SS[NoneCount]=S[NoneCount]

    No=NoneCount
    index=Noneindex
    while No>0:
        if No==NoneCount:SSS=list(SS)
        if SS[No]+numberA[I[index[No-1]-1]]+space<=30:
            SS[No-1] = SS[No-1]-space-numberA[I[index[No-1]-1]]
            SS[No] = SS[No] + space + numberA[I[index[No-1]-1]]
            I[index[No-1]-1],I[index[No-1]]=I[index[No-1]],I[index[No-1]-1]
            index[No-1]-=1
            No-=1
            an=ans(SS,W)
            if No==-1:No=NoneCount
            if an<min:
                min=an
        else: 
            No-=1
            if No==-1:No=NoneCount
        if No==0 and SSS==SS: break ##SS에 변화가 없으면 더이상의 경우의 수는 없음.

        # if No>0 and SS[No-1]<SS[No] and SS[No] + space + numberA[I[Noneindex[No]-1]]<30:
        #     SS[No-1] = SS[Noneindex[No]-1]-space-numberA[I[Noneindex[No]-1]]
        #     SS[No] = SS[Noneindex[No]] + space + numberA[I[Noneindex[No]-1]]
        #     I[Noneindex[No]-1],I[Noneindex[No]]=I[Noneindex[No]],I[Noneindex[No]-1]
        #     an=ans(SS,W)
        #     if an<min:min=an

    return penalty(numberA, S, I, Noneindex,W, min)    


def ans(S,W):
    n=len(S)-1
    sum=0
    while n>=0:
        sum+=(W-S[n])**3
        n-=1
    return sum

W = int(input())
words = input().split()
print(words)
numberA = make_number(words)
print(numberA)
S,I,Noneindex=divide(numberA, W)
print(S)
print(I)
print(Noneindex)
min=ans(S, W)
min=penalty(numberA, S, I,Noneindex, W,min)
print(min)
