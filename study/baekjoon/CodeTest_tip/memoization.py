"""
동적 계획법 : 큰 문제를 작은 문제로 나누어서 하나씩 해결해 나가라.
1. for loop
2. 재귀 : 문제점 - 중복되는 계산이 많음. 시간 복잡도 높다. 
          해결법 = 기록해라. 이전에 계산 했던건지 check!!!!
"""

memo = [-1, -1, -1, ...]

def padovan(n):
    if memo[n] != -1:
        return memo[n]
    if n <= 3:
        memo[n] = 1
    else:
        memo[n] = padovan(n - 2) + padovan(n - 3)
        print(memo[n])

    return memo[n]