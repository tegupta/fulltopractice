low=int(input("Enter lower limit of number: "))
upper=int(input("Enter upper limit of number: "))
n=int(input("Enter by which number you want to divide:"))
for i in range(low,upper):
    if(i%n==0):
        print(i)