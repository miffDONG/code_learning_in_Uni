n = int(input())
li = []
for i in range(n):
    temp = list(map(int,input().split()))
    li.append(temp)

answer = 0
# list 범위 지정 주목

for i in range(n-2):
    for j in range(n-2): #시작점 지정
        temp = 0
        for row in li[i:i+3]: # 시작점으로 부터 범위 지정 후 덧셈
            temp += sum(row[j:j+3])
        answer = max(answer,temp)

print(answer)