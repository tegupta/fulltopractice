a=[]
even=[]
odd=[]
n=int(input("Enter number of elements:"))
for i in range(0,n):
    b=int(input("Enter number:"))
    a.append(b)

for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
        
print(even)
print(odd)