num = list(map(int,input().split()))

count = 0
same = 0
money = 0
for i in range(0,len(num)):
    for k in range(i+1,len(num)):
        if num[i]==num[k]:
            count+=1
            same = num[i]
if count == 1:
    count+=1

if count == 3:
    money = 10000 + same * 1000
elif count == 2:
    money = 1000 + same *100
else:
    maxi = max(num)
    money = maxi * 100

print(money)