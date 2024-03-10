def reps(A):
    if A[0]<A[len(A)-1]:
        return 0

    mid = len(A)//2
    first,left= 0,mid//2
    last,right = len(A)-1, len(A)-1-mid//2
		
		#위에서 회전의 없는경우를 확인 했으므로 회전이 반드시 있음
		#오름차순 정렬된 것이 회전된 것이므로 A[i]>A[i+1]인 경계가 존재, i의 index번호를 찾는 알고리즘
		#경계가 바깥쪽에 있을수록 비교횟수가 적고 안쪽에 있을수록 비교횟수 증가.
		# B.C T(n) = T(1/2)+cn -- 4구간 중 first~left, right~last 구간 추출하므로 절반씩 줄이게 됌. O(logn)
		#	
		#[first~left~mid~right~last]구간에서 
    while A[left]>A[right]:
        first,last=left,right
        left=first+(mid-first)//2
        right=last-(last-mid)//2
        if (mid-first)//2==0 and (last-mid)//2==0:
            break
    
    
    while first<left:
        if A[first]<A[first+1]:
            first+=1
        else:
            break
    while right<last:
        if A[right]<A[right+1]:
            right+=1
        else:
            break
					
    if first==left: 
        if right==last:
            result = len(A)-1-first # mid-1 = 바뀌는 구간
        else: 
            result = len(A)-1-right	# 
    else:
        result = len(A)-1-first
    return result
        


# A = list(map(int,input().split()))
A=[5,6,1,2,3,4]
print(reps(A))