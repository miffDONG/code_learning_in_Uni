from collections import deque

"""
백준 : 숨바꼭질

문제 : 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

조건 : 1. 동생은 가만히 있음.
       2. 수빈이 이동 방식 ( x-1 , x+1 , x*2 )


? 수행시간 Tree - T(n) = 3T(n) + c
"""

"""
풀이 : bfs 너비 우선 탐색 
선택 이유 : 최단시간을 찾기 위한 algorithm

출력 : 해당 값의 Tree level 
"""

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()

        if x == k:    # 동생 발견
            print(dist[x])
            break

        for nx in (x-1,x+1,x*2): 
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)

MAX = 10 ** 5
dist = [0]*(MAX+1)
n,k = map(int,input().split())

bfs() 



"""

추가학습 not list[] 출력
기본적으로 값이 존재하면 False
없으면 True 

None -> True
False -> True
number -> False
True -> False

"""