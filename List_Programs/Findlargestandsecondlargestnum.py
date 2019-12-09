a=[]
n=int(input("Enter number of elements"))
for i in range(0,n):
    b=int(input("Enter Number:"))
    a.append(b)
a.sort()
print(a[-1],a[-2])