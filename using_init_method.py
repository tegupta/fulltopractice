
class Emp(object):
    def __init__(self,name,salary):
        self.name=name 
        self.salary=salary
        return None
    def display(self):
        print(f"The name is: {self.name}\nThe salary is:{self.salary}")
        return None

emp1=Emp('Ramu', 54000)
emp1.display()