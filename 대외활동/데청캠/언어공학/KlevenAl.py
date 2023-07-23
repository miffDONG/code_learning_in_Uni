from MinEditDistance import KlevenshteinDistance
from Kseperator import decompose

str1 = '하늘을 나는 새를 봤다'
str2 = '하늘을 나는 새를 보았다'

dec1 = decompose(str1)
dec2 = decompose(str2)

print(dec1)
answer = KlevenshteinDistance(dec1,dec2)
print(answer)


"""
+ 기능 

morpheme 단위 나눌 필요성
'하늘을 나는 새를 보았다'
-> 하늘 을 날 는 새 를 보아 ㅆ다

'하늘을 나는 새를 봤다'
-> 하늘 을 날 는 새 를 보아 ㅆ다

'하늘을 나는 새랑 봤다'
-> 하늘 을 날 는 새 랑 보아 ㅆ다

""" 
