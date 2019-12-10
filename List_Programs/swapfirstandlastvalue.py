a=[]
n=int(input("Enter the size of the list:"))
for i in range(0,n):
    num=int(input("Enter element" + str(i+1) + ":"))
    a.append(num)

temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print(a)