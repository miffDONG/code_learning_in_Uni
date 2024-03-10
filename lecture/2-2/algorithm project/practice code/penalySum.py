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
        else:
            j+=1
            I.append(None)
    return S,I

    ####################################################################################
    ##### 앞으로 S를 최대한 밀어넣었는데, None 앞 값을 뒤로 한번씩 밀으면서 3제곱 값을 구하고
    # 작은 값은 MIN에 계속 초기화/

def penalty(numberA,S,I,W,min):
    l=len(I)
    space=1
    k=l-2
    NoneCount=len(S)-1
    while I[k]!=None:k-=1
    #탈출조건 / 맨 뒤 그룹의 합이 w보다 커지는 경우는 더이상 이동 값이 없을 때로 판단.
    if numberA[I[k-1]]+space+S[NoneCount]>W:
        return min

    
    while k>0 and NoneCount >0:
        while I[k]!=None:
            k-=1
        # 앞 그룹이 뒷 그룹보다 크면 하나씩 넘겨봄.
        while S[NoneCount-1]>S[NoneCount]:
            if S[NoneCount]+numberA[I[k-1]]+space<=30:
                S[NoneCount-1] = S[NoneCount-1]-space-numberA[I[k-1]]
                S[NoneCount] = S[NoneCount] + space + numberA[I[k-1]]
                I[k-1],I[k]=I[k],I[k-1]
                k-=1
                an=ans(S,W)
                if an<min:min=an
            else: break
        NoneCount-=1   
        if NoneCount>0 and S[NoneCount-1]<S[NoneCount] and S[NoneCount] + space + numberA[I[k-1]]<30:
            k-=1
            while I[k]!=None:
                k-=1
            S[NoneCount-1] = S[NoneCount-1]-space-numberA[I[k-1]]
            S[NoneCount] = S[NoneCount] + space + numberA[I[k-1]]
            I[k-1],I[k]=I[k],I[k-1]
            an=ans(S,W)
            if an<min:min=an
        k-=1 
    return penalty(numberA, S, I, W, min)    
    # 중간 값을 앞 뒤 어디에 더해야 할지 정해야할 때, 함수를 어디에 넣어야할지.append ? plus ? 
    # 조건은? A[n-1]이 A[n-2]와 A[n] 중 어디에 더해도 성립할때,
    # 작은문제로 생각했을 때,


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
S,I=divide(numberA, W)
print(S)
print(I)
min=ans(S, W)
min=penalty(numberA, S, I, W,min)
print(min)
