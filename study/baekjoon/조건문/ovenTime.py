hour, min = map(int, input().split())
time = int(input())

next_min = min + time
if next_min%60 == 0:
    min = 0 
else:
    min = next_min % 60

x = next_min // 60
hour += x

if hour > 23:
    hour -= 24 
else: pass

print(hour, min)