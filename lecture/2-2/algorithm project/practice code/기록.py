#교재에 나온대로 x,y,w,z구역이라 하겠다.
def find_index(a,n,k):
    mom_index=n//2 
    second_mom_index=0
    rx,ry=0,0
    if a[mom_index][mom_index]<k:
        if n-2==mom_index:second_mom_index=mom_index-1
        else:second_mom_index=n-1

    #mom을 두개설정. 범위를 정할때 기준 피벗 = mom_index
    #second_mom_index는 k범위를 정하기 위함.
    #사각형을 만들건데, (second-n ~ mom+n) 길이의 정사각형을 만들예정.
    while abs(second_mom_index-mom_index)!=1:
        if k<a[mom_index][mom_index]:
            second_mom_index=mom_index
            mom_index=mom_index//2
        elif k==a[mom_index][mom_index]: 
            return mom_index,mom_index
        else:
            second_mom_index=mom_index
            mom_index=(mom_index+(n-1))//2
    
    #계산을 위해 second_mom<mom 으로 설정
    if mom_index<second_mom_index and n-1!=mom_index: 
        temp = mom_index
        mom_index=second_mom_index
        second_mom_index=temp

    # k<second_mom_index일때
    # x,y,z 구역 탐색
    if second_mom_index>k:
        x=second_mom_index-1
        y=second_mom_index-1
        while x<mom_index+1 and y<mom_index+1:
            # if y<second_mom_index:
            for i in range(x,mom_index+2):
                if a[i][y]==k: return i,y
                else: continue
            while y<mom_index+2:
                if a[second_mom_index-1][y]==k: return x,y
                else: y+=1
        return -1,-1

    # k>mom_index일때
    # w,y,z 구역 탐색
    if mom_index<k:
        x=mom_index+1
        y=mom_index+1
        while x>second_mom_index-1 and y>second_mom_index-1:
            for i in range(second_mom_index-1,x+1):
                if a[i][y]==k: return i,y
                else: continue
            while y>second_mom_index-2:
                if a[mom_index+1][y]==k: return x,y
                else: y-=1
        return -1,-1

    return -1,-1

