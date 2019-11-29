n=int(input("Enter number"))
a=[]
for i in range (2,n):
    if(n%i==0):
        a.append(i)

a.sort()
print(" divisor are :",a)    
print(" smallest divisor is :",a[0])    
