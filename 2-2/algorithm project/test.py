a=[1,2,3,4,5,6,7]
b=[1,2,3,4,5,6,7]
c=list(b)

print(c)
b.pop()
print(c)
if b==a:
    print("오예")