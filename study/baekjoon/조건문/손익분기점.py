fix, cost, sell= map(int,input().split())
count=0

if cost<sell:
    count = fix//(sell-cost) +1
else: count=-1


print(count)