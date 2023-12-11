
# def push_place1(A,k,push_number):
#     f_half = 0
#     half=k
#     leng=k
#     if k>5:
#         half = k//2
#         leng = leng//2
#     while abs(f_half-half)>5:
#         leng = leng//2
#         if push_number > A[half]:
#             if f_half ==0: 
#                 f_half = k//2
#             else:pass

#             if push_number < A[half+(leng)]: 
#                 f_half = //
#                 half = f_half+(leng)
#             else:
#                 half = k
#                 f_half = half-(leng)
#         else:
#             if push_number < A[half-(leng)]:
#                 f_half = 0
#                 half = half-(leng)
#             else:
#                 f_half = half-(leng)
#     for j in range(f_half,k):
#         if push_number > A[j]:
#             pass
#         else:
#             return j
    
def push_place2(A,k,push_number):
    for j in range(0,k):
        if push_number > A[j]:
            pass
        else:
            return j

def push_place3(A,k,push_number):
    front = 0
    half = k//2
    last = k
    mid = A[k//2]
    leng = k//2
    
    while abs(half -front)>5 or abs(last-half)>5:
        f_h = (front+half)//2
        h_l = (half+last)//2
        if push_number > A[half]:
            if push_number < A[h_l]:
                front = half
                last = h_l
            else:
                front = h_l
            half = ((front+last)//2)                
        else:
            if push_number < A[f_h]:
                last = f_h
            else:
                front = f_h
                last = half
            half = ((front+last)//2)

    for j in range(front,k):
        if push_number > A[j]:
            pass
        else:
            return j

A=[1,2,3,4,5,6,7,8,9,10,32,33,39,42]
# A =[9,1,3,2,7,0,-2,4,5]
a=push_place3(A,len(A),40)
b=push_place2(A,len(A),40)
print(type(a),type(b))
print(a,b)