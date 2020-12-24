class Employee():
    raiseAmount = 1.04
    empNumber = 0
    def __init__(self, first, last, salary, raiseAmount = 0.0):
        self.first= first
        self.last= last
        self.salary= salary
        self.email = first + '.' + last + '@gmail.com'
        self.raiseAmount = raiseAmount or Employee.raiseAmount
        Employee.empNumber +=1
    def fullname(self):
        return f'{self.first}  {self.last}'

    def apply_raise(self):
        self.salary = self.salary * self.raiseAmount

emp1 = Employee('Ahmed', 'Atef', 10000, 1.06)

emp2 = Employee('Ali', 'Alex', 20000)

print(Employee.__dict__)
print(emp1.salary)
emp1.apply_raise()
print(emp1.salary)

print(emp2.__dict__)
print(emp2.salary)
emp2.raiseAmount = 1.02
emp2.apply_raise()
print(emp2.salary)
print(emp2.__dict__)


print(f'\nNumber of employee is {Employee.empNumber}')