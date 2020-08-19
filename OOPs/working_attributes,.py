class Emp:
    def get_name_age_salary(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        self.display_details()
        return None
    def display_details(self):
        print(f'The name is: {self.name}\n The age is: {self.age}\n The salary is: {self.salary}')
        return None


emp1=Emp()
emp2=Emp()

emp1.get_name_age_salary('john',34,45000)
emp2.get_name_age_salary('cliton',25,54000)

#print(emp2.age)

#emp1.display_details()