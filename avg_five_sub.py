n1=int(input("Enter Marks of first subject:"))
n2=int(input("Enter Marks of second subject:"))
n3=int(input("Enter Marks of Third subject:"))
n4=int(input("Enter Marks of fourth subject:"))
n5=int(input("Enter Marks of fifth subject:"))
avg=(n1+n2+n3+n4+n5)/5

if (avg>=90):
    print("A")
elif(avg>=80&avg<90):
    print("B")
elif (avg>=70&avg<80):
    print("C")
elif (avg>=60&avg<70):
    print("D")
else:
    print("E")
    