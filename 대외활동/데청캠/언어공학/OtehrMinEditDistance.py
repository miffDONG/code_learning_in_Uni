s1 = 'cake'
s2 = 'cat'

word1 = ' ' + s1
word2 = ' ' + s2

n,m = len(word1),len(word2)

score1 = [[0 for _ in range(n)] for _ in range(m)]
score2 = [[0 for _ in range(n)] for _ in range(m)]

for i in range(n):
    score1[0][i] = score2[0][i] = i
for i in range(n):
    score2[0][i] = score2[i][0] = i 

#Minimum Edit Distance
for y in range(1,m):
    for x in range(1,n):
        if word1[x] == word2[y]:
            score1[y][x] = score2[y-1][x-1]
        else:
            score1[y][x] = min(score1[y-1][x-1], score1[y-1][x],score1[y][x-1])+1

print(score1[m-1],[n-1])

#Levenshtein Distance
for y in range(1,m):
    for x in range(1,n):
        if word1[x] == word2[y]:
            cost = 0
        else:
            cost = 2
        score2[y][x] = min(score2[y-1][x-1]+cost, score2[y-1][x]+1,score2[y][x-1]+1)

print(score2[m-1],[n-1])
