from MinEditDistance import KlevenshteinDistance
from Kseperator import decompose

str1 = '김현동'
str2 = '김삼순'

dec1 = decompose(str1)
dec2 = decompose(str2)

print(dec1)
answer = KlevenshteinDistance(dec1,dec2)
print(answer)
