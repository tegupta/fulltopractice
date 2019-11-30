import math
n=int(input("Enter number:"))
a=[]
for i in range (1,n+1):
    print(i,end="")
    if(i<n):
        print('+',end="")
    a.append(i)
print ("=",sum(a))

print()