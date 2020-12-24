import datetime

class Employee():
    raise_amount = 1.04
    emp_number = 0
    def __init__(self, first, last, salary):
        self.first= first
        self.last= last
        self.salary= salary
        self.email = first + '.' + last + '@gmail.com'
        Employee.emp_number +=1

    def fullname(self):
        return f'{self.first}  {self.last}'

    def apply_raise(self):
        self.salary = self.salary * self.raise_amount

    def __repr__(self): #Used to show detailed representaion for debugging
        return f'Employee ({self.first}, {self.last}, {self.salary})'

    def __str__(self): #used to show abstrach data for the user
        return f'{self.first}, {self.last}, {self.email}'

    def __add__(self, other): #add feature to the class
        return self.salary + other.salary

    def __len__(self):
        return len(self.fullname())



emp1 = Employee('Ahmed', 'Atef', 10000 )
emp2 = Employee('Ali', 'Alex', 20000 )

emp1.first = 'Shady'
print(emp1.email)  #Ahmed.Atef@gmail.com

print(emp1.__len__()) #the magic method len has been added
print(len(emp2))

print(emp1.__repr__())
print(emp1.__str__())
print(emp1 + emp2) # add magic method