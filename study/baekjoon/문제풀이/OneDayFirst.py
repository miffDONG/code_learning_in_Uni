n,m = map(int,input().split())
arr = list(map(int,input().split()))

mx = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum = arr[i] + arr[j] + arr[k]
            if sum > m:
                pass
            else:
                mx = max(mx,sum)

print(mx)