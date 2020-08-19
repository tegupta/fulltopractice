class Emp:
    count=0
    def __init__(self):
        Emp.count=Emp.count+1
        return None
    def display(self):
     print('This is a display method')
     return None

emp1=Emp()
emp2=Emp()
print('the number of objects created from Emp class are:', Emp.count)

#emp1.display()
#emp2.display()