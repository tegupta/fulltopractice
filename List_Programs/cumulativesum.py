a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    a.append(element)

# b=[sum(a[0:x+1]) for x in range(0,len(a))]
# print(a)
# print(b)
s=0
for x in range(0,len(a)):
    s=s+a[x]
    print(s, sep="")
