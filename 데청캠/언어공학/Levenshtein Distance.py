def levenshteinDistance(s1,s2):
    rows, columns = len(s1)+1, len(s2)+1
    arr = [list(range(columns)) if not i else [i]+[0]*(columns-1) for i in range(rows)]
    

    
    for x in range(1,rows):
        for y in range(1,columns):
            if s1[x-1] == s2[y-1]:
                arr[x][y] = arr[x-1][y-1]
            else:
                arr[x][y] = min(arr[x-1][y]+1,arr[x-1][y-1]+2,arr[x][y-1]+1)
            
    for r in arr:
        print(r)

    return arr[len(s1)][len(s2)]


s1 = 'cake'
s2 = 'cat'

answer = levenshteinDistance(s1,s2)

print(answer)
