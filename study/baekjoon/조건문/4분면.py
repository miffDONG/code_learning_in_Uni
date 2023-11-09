x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        quad = 1
    else: quad = 4
else:
    if y>0:
        quad = 2
    else: quad = 3

print(quad)
