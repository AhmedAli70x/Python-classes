class Employee():
    def __init__(self, first, last, salary):
        self.first= first
        self.last= last
        self.salary= salary
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        # return '{} {}'.format(self.first, self.last)

        return f'{self.first}  {self.last}'



emp1 = Employee('Ahmed', 'Atef', 10000)
emp2 = Employee('Ali', 'Alex', 22000)

fullName= Employee.fullname(emp2)
print(emp1.fullname())
print(emp2.salary)
print(emp1.email)
print(fullName)