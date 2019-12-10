a=[]
n=int(input("Enter number of elements:"))
for i in range(0,n):
    b=input("Enter Values :")
    a.append(b)

a.sort(key=len)
print(a)