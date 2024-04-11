"""
1이상 100이하의 숫자로만 이루어져 있는 n * n 크기의 격자 정보가 주어집니다.

이때 행복한 수열이라는 것은 다음과 같이 정의됩니다.

행복한 수열 = 연속하여 m개 이상의 동일한 원소가 나오는 순간이 존재하는 수열
n * n 크기의 격자 정보가 주어졌을 때 각 행마다 봤을 때 나오는 n개의 수열과, 각 열마다 봤을 때 나올 수 있는 n개의 수열을 포함하여 총 2n개의 수열 중 행복한 수열의 개수를 세서 출력하는 프로그램을 작성해보세요.

예를 들어, 다음과 같은 경우라면, 첫 번째 행을 골랐을 경우와 첫 번째 열을 골랐을 경우에만 행복한 수열이 되므로, 총 행복한 수열의 수는 2개가 됩니다.
"""

# n,m = map(int,input().split())
# li = [list(map(int, input().split())) for _ in range(n)]

# happy_count = 0

# for i in li:
#     continue_num = 0
#     count = 1
#     high = 1
#     for j in i:
#         if continue_num == 0:
#             continue_num = j
#         elif continue_num != j:
#             continue_num = j
#             count = 1
#         elif continue_num == j:
#             count+=1
#         if high < count: 
#             high = count
#         if high >= m:
#             happy_count+=1
#             break
    
# for i in range(n):
#     continue_num = 0
#     count = 1
#     high = 1
#     for j in range(n):
#         now_num = li[j][i]
#         if continue_num == 0:
#             continue_num = now_num
#         elif continue_num != now_num:
#             continue_num = now_num
#             count = 1
#         elif continue_num == now_num:
#             count+=1
#         if high < count: 
#             high = count
#         if high >= m:
#             happy_count+=1
#             break 

# print(happy_count)

# 다른풀이 

import sys
sys.stdin=open('input.txt','r')

if __name__=="__main__":
    n,m=map(int,input().split())
    li = []
    happy_count = 0
    # 첫 row 입력을 받는 for문을 지나치지 않고 활용.
    for _ in range(n):
        row = list(map(int,input().split()))
        li.append(row)
        for i in range(n-m+1):
            if row[i:i+m].count(row[i]) == m:
                happy_count+=1
                break

    # iterable 자료형 unpacking 하는 연산자 *
    # [[1,2,3],[4,5,6],[7,8,9]] -> [1,2,3] [4,5,6] [7,8,9]
    # zip 명령어로 열 묶기 
    for cow in zip(*li):
        for i in range(n-m+1):
            if cow[i:i+m].count(cow[i]) == m:
                happy_count+=1
                break

    print(happy_count)