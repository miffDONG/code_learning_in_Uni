

#minimum edit distance
def minDist(s1,s2):
    rows, columns = len(s1)+1, len(s2)+1
    arr = [list(range(columns)) if not i else [i]+[0]*(columns-1) for i in range(rows)]
    

    
    for x in range(1,rows):
        for y in range(1,columns):
            if s1[x-1] == s2[y-1]:
                arr[x][y] = arr[x-1][y-1]
            else:
                arr[x][y] = min(arr[x-1][y],arr[x-1][y-1],arr[x][y-1])+1
            
    for r in arr:
        print(r)

    return arr[len(s1)][len(s2)]

def levenshteinDistance(s1,s2):
    rows, columns = len(s1)+1, len(s2)+1
    arr = [list(range(columns)) if not i else [i]+[0]*(columns-1) for i in range(rows)]
    
    for x in range(1,rows):
        for y in range(1,columns):
            if s1[x-1] == s2[y-1]:
                arr[x][y] = arr[x-1][y-1]
            else:
                arr[x][y] = min(arr[x-1][y-1]+2,arr[x-1][y]+1,arr[x][y-1]+1)
            
    for r in arr:
        print(r)

    return arr[len(s1)][len(s2)]



def KlevenshteinDistance(s1,s2):
    str1 = [element for row in s1 for element in row]
    str2 = [element for row in s2 for element in row]
    rows, columns = len(str1)+1, len(str2)+1
    arr = [list(range(columns)) if not i else [i]+[0]*(columns-1) for i in range(rows)]
    
    for x in range(1,rows):
        for y in range(1,columns):
            if str1[x-1] == str2[y-1]:
                arr[x][y] = arr[x-1][y-1]
            else:
                arr[x][y] = min(arr[x-1][y-1]+2,arr[x-1][y]+1,arr[x][y-1]+1)
            
    for r in arr:
        print(r)

    return arr[len(str1)][len(str2)]


s1 = '김현동'
s2 = '김삼순'

KlevenshteinDistance(s1,s2)


# s1 = 'cake'
# s2 = 'cat'

# answer = levenshteinDistance(s1,s2)
# print(answer)
# answer = minDist(s1,s2)

# print(answer)
