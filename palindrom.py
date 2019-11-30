num=int(input("Enter number:"))
temp=num
sum=0
while(num>0):
    n=num%10
    sum=sum*10+n
    num=num//10
    
if(temp==sum):
    print("Palindrom")
else:
    print("BOOOOPSSSS!!!!!")