
#class Emp:

class Emp(object):
    def name_salary(self,name,salary):
        self.name=name 
        self.salary=salary
        return None
    def display(self):
        print(f"The name is: {self.name}\nThe salary is:{self.salary}")
        return None


emp1=Emp()
emp1.name_salary('Ram', 56000)

emp2=Emp()
emp2.name_salary('Deepak', 1000000)
emp1.display()
emp2.display()