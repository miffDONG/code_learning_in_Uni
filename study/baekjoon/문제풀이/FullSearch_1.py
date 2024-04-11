"""
N * N 크기의 격자 정보가 주어집니다. 
이때 해당 위치에 동전이 있다면 1, 없다면 0이 주어집니다. 
N * N 격자를 벗어나지 않도록 3 * 3 크기의 격자를 적절하게 잘 잡아서 해당 범위 안에 들어있는 동전의 개수를 최대로 하는 프로그램을 작성해보세요.
"""

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