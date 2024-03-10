def find_index(A,n,k):
    #x의 mom
    #y의 mom 겹치는 부분을 찾아 그 주변 정사각형 탐색
    x_mom=n//2
    y_mom=n//2
    s_x_mom, s,_y_mom = 0,0     #s는 second의 줄임말로 중간값으로 줄이기 위함
    xfirst=0
    yfirst=0
    #s_x_mom 초기설정 , s_y_mom 초기설정
    if A[x_mom][y_mom]==k: return x_mom,y_mom
    elif A[x_mom][y_mom]>k:
        s_x_mom=x_mom//2
        s_y_mom=y_mom//2

    elif A[x_mom][y_mom]<k: 
        if n-2==x_mom:
            s_x_mom = x_mom-1
            s_y_mom = y_mom-1
        else: 
            s_x_mom = (n-1)+x_mom//2
            s_y_mom = (n-1)+y_mom//2

    # second값을 항상 왼쪽, 위쪽에 둘것 (계산을 위해)
    if s_x_mom>x_mom:
        temp = s_x_mom
        s_x_mom=x_mom
        x_mom=temp

    #x값 조절
    while (s_x_mom-x_mom)!=1 and x_mom-s_x_mom>2:
        if A[s_x_mom][s_y_mom]>K: 

# a=[[2,5,10,19],[3,8,16,19],[7,20,20,32],[13,25,37,44]]
a=[[-24,-9,-8,18],[-21,-7,3,19],[-20,-4,7,22],[-10,-2,15,25]]
x,y=find_index(a, 4, -2)
print(f"({x}, {y})")