#교재에 나온대로 x,y,w,z구역이라 하겠다.
def find_index(a,n,k):
    mom_index=n//2 
    second_mom_index=0
    if a[mom_index][mom_index]<k:
        if n-2==mom_index:second_mom_index=mom_index-1
        else:second_mom_index=n-1

    #mom을 두개설정. 범위를 정할때 기준 피벗 = mom_index
    #second_mom_index는 k범위를 정하기 위함.
    #사각형을 만들건데, (second-n ~ mom+n) 길이의 정사각형을 만들예정.
    while abs(second_mom_index-mom_index)!=1:
        if k<a[mom_index][mom_index]:
            if second_mom_index==1 or mom_index==1:
                second_mom_index=1
                mom_index=2
            else:
                second_mom_index=mom_index
                mom_index=mom_index//2
        elif k==a[mom_index][mom_index]: 
            return mom_index,mom_index
        else:
            if second_mom_index==n-2 or mom_index==n-2:
                mom_index=n-2
                second_mom_index=n-3
            else:
                second_mom_index=mom_index
                mom_index=(mom_index+(n-1))//2
    
    #계산을 위해 second_mom<mom 으로 설정
    if mom_index<second_mom_index and n-1!=mom_index: 
        temp = mom_index
        mom_index=second_mom_index
        second_mom_index=temp

    if a[mom_index][mom_index]==k: return mom_index,mom_index

    if a[second_mom_index][second_mom_index]>k:
        x=second_mom_index-1
        y=second_mom_index-1
        #second 윗라인
        while x<n and y<n:
            if a[x][y]==k:return x,y
            else: y+=1
        #second 오른쪽라인
        x=second_mom_index
        y=mom_index
        while x>-1 and y>-1:
            if a[x][y]==k:return x,y
            else: y-=1
        #second 왼쪽라인(아래로)
        y=second_mom_index-1
        x=second_mom_index-1
        while y<n and x<n:
            if a[x][y]==k:return x,y
            else:x+=1
        #second아랫라인
        x=mom_index
        y=second_mom_index
        while y>-1 and x>-1:
            if a[x][y]==k:return x,y
            else:x-=1

    # k>A[mom_index]일때
    # w,y,z 구역 탐색
    if a[mom_index][mom_index]<k:
        x=mom_index+1
        y=mom_index
        #mom 아래라인
        while x<n and y<n:
            if a[x][y]==k:return x,y
            else:y+=1
        #mom 왼쪽라인보기
        x=mom_index
        y=mom_index-1
        while x<n and y<n:
            if a[x][y]==k:return x,y
            else:y+=1

        x=mom_index+1
        y=mom_index+2
        
        while y<n and x<n:
            if a[x][y]==k:return x,y
            else:x+=1

        x=mom_index-1
        y=mom_index
        while y<n and x<n:
            if a[x][y]==k:return x,y
            else:x+=1

    if k>a[second_mom_index][second_mom_index] and k<a[mom_index][mom_index]:
        x=0
        y=second_mom_index+1
        while y<n and x<mom_index:
            if a[x][y]==k: return x,y
            x+=1
            if x==mom_index:
                y+=1
                x=0

        x=second_mom_index
        y=second_mom_index        
        while y>=0 and x<n:
            if a[x][y]==k: return x,y
            y-=1
            if y==-1:
                y=second_mom_index
                x+=1

    return -1,-1


##psudo코드 작성 
# 일단 범위를 줄일거임 MoM 방식으로 그런데 



a=[[1,2,3,4,5,6,7],[11,12,13,14,15,16,17],[21,22,23,24,25,26,27],[31,32,33,34,35,36,37],[41,42,43,44,45,46,47],[51,52,53,54,55,56,57],[61,62,63,64,65,66,67],[71,72,73,74,75,76,77]]
# a=[[-24,-9,-8,18],[-21,-7,3,19],[-20,-4,7,22],[-10,-2,15,25]]
x,y=find_index(a, 7, 57)
print(f"({x}, {y})")


    # k<second_mom_index일때
    # x,y,z 구역 탐색
    # if a[second_mom_index][second_mom_index]>k:
    #     x=second_mom_index-1
    #     y=second_mom_index-1
    #     while x<mom_index+1 and y<mom_index+1:
    #         for i in range(x,mom_index+2):
    #             if a[i][y]==k: return i,y
    #             else: continue
    #         while y<mom_index+2:
    #             if a[second_mom_index-1][y]==k: return x,y
    #             else: y+=1
    #     return -1,-1
