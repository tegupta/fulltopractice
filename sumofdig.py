n=int(input("Enter number:"))
sum=0
while(n>0):
    temp=n%10
    sum=sum+temp
    n=n//10

print(sum)
