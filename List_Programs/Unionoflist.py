lst1=[]
lst2=[]

n=int(input("Enter the size of list:"))
for i in range(0,n):
    num=input("Enter values:")
    lst1.append(num)

    
n=int(input("Enter the size of list:"))
for i in range(0,n):
    num=input("Enter values:")
    lst2.append(num)

union=list(set().union(lst1,lst2))
print(union)