def push_place(A,k,push_number):    
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
    
def get_sum(A):            
    sum = A[0]
    n=len(A)
    a_min, b_min, b_max = A[0],A[0],A[0]    
    stack = [A[0]]
    que_a = []
    que_b = [A[0]]
    k=1
    sum_n = 0
    for i in range(1,n):
        stack.append(A[i])
        k = i//3+1
        if a_min > A[i]:
            a_min = A[i]
            que_a.insert(0,A[i])


        elif a_min < A[i]:
            if A[i] < 0:
                que_a.insert(push_place(que_a,len(que_a),A[i]),A[i])

            else:
                if b_min > A[i]:
                    if que_a[-1] > A[i]:
                        que_a.insert(push_place(que_a,len(que_a),A[i]),A[i])
                    else:
                        b_min = A[i]
                        que_b.insert(0,A[i])


                elif b_min < A[i]:
                    if b_max > A[i]:
                        que_b.insert(push_place(que_b,len(que_b),A[i]),A[i])
                        b_min = que_b[1]
                        que_a.append(que_b.pop(0))
                    
                    else:
                        que_b.append(A[i])
                        b_min = que_b[1]
                        que_a.append(que_b.pop(0))
                        b_max = A[i]

        if len(que_a) < k:
            sum_n = que_b[k-len(que_a)-1]
        else:sum_n = que_a[k-1]
        sum = sum + sum_n

    return sum