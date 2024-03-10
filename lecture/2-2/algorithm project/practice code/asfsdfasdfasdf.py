#숫자화
def make_number(words): #문장에서 띄어쓰기를 기준으로 전,후 문자열 수로 재정의
    n=len(words)
    number = 0
    list=[]
    for i in range(0,n):
        list.append(len(words[i]))
    return list



def penalty(numberA,W):    # 숫자로 재정의 된 리스트로 함수 정의
    n=len(numberA)
    space=1
    S=[]
    I=[]
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
    ####################################################################################
    ##### 지금 S 상황. 앞에 원소에 최대한 많은 수가 더해지도록 시스템 .
    ##### 전 후 S 원소의 값 차이를 줄일거임. 
    l=len(I)
    k=l-2
    NoneCount=len(S)-1
    while k>0 and NoneCount >0:
        while I[k]!=None:
            k-=1
        while S[NoneCount-1]>S[NoneCount]:
            if abs(S[NoneCount]-S[NoneCount-1])>abs( (S[NoneCount-1]-space-numberA[I[k-1]]) - (S[NoneCount]+space+numberA[I[k-1]]) ):
                S[NoneCount-1] = S[NoneCount-1]-space-numberA[I[k-1]]
                S[NoneCount] = S[NoneCount]+space+numberA[I[k-1]]
                k-=1
            else: break
        NoneCount-=1        
    return S
    # 중간 값을 앞 뒤 어디에 더해야 할지 정해야할 때, 함수를 어디에 넣어야할지.append ? plus ? 
    # 조건은? A[n-1]이 A[n-2]와 A[n] 중 어디에 더해도 성립할때,
    # 작은문제로 생각했을 때,

W = int(input())
words = input().split()

numberA = make_number(words)
S=penalty(numberA, W)
n=len(S)-1
sum=0
while n>=0:
    sum+=(W-S[n])**3
    n-=1
print(sum)

# code below