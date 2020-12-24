import datetime

class Employee():
    raise_amount = 1.04
    def __init__(self, first, last, salary):
        self.first= first
        self.last= last
        self.salary= salary


    @property #used to call the property without parenthesis
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'
    @property
    def fullname(self):
        return f'{self.first}  {self.last}'

    def apply_raise(self):
        self.salary = self.salary * Employee.raise_amount

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')

    @fullname.deleter
    def delete_name(self):
        self.first = None
        self.last = None
        print("\nName deleted")

emp1 = Employee('Ahmed', 'Atef', 10000 )
emp2 = Employee('Ali', 'Alex', 20000 )
print(emp1.first)
print(emp1.email)
emp1.apply_raise()
print(emp1.salary)

emp1.fullname  = 'Mohsen Mohamed'

print('\n'+emp1.first)
print(emp1.email)
print(emp1.fullname)

del emp2.delete_name
print(emp2.first)

