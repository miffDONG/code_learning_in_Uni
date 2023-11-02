"""
point 
체스판 자르기
(0,0) -> Black && White
"""

n,m = map(int, input().split())
board = [input() for _ in range(n)]
board = [list(string) for string in board]
result=[]

for i in range(n-7):
    for j in range(m-7):
        draw1 = 0
        draw2 = 0

        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y) % 2 == 0:
                    if board[x][y] != 'B':
                        draw1 +=1
                    if board[x][y] != 'W':
                        draw2 +=1
                else:
                    if board[x][y] != 'W':
                        draw1 += 1
                    if board[x][y] != 'B':
                        draw2 += 1

        result.append(draw1)
        result.append(draw2)

print(min(result))

