# list1=[1,2,3,4,5,6]
# result=[(val,pow(val,2)) for val in list1]
# print(result)

lower=int(input("Enter the lower limit:"))
upper=int(input("Enter the upper limit:"))

list1=[(x,x**2) for x in range(lower,upper+1)]
print(list1)