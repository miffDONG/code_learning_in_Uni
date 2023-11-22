arr = []
while True: 
    try:
        line = list(map(int,input().split()))
        _sum = [line[0],line[0]+line[1]]
        arr.append(_sum)
    except:
        break

arr.sort(key = lambda x : x[1])

for i in range(len(arr)):
    print(arr[i][0], end=' ')