def solve(A):
    n = len(A)
    s = 0
    while len(A)>0:
        x = A.pop(0)
        if x%2:
            s+=x
    return s

A=[1,2,3,4,5]
print(solve(A))