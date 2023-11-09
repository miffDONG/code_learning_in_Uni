hour, min = map(int, input().split())

if min > 45:
    min -= 45
else:
    if min >= 45:
        min -= 45
    else: 
        if hour == 0:
            hour = 23 
        else: hour -=1

        min = min + 60 - 45        


print(hour, min)