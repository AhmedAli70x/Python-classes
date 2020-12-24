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

class Developer(Employee):
    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last , salary, emps = None):
        super().__init__(first, last, salary)
        self.emps = emps or []

    def add_emp(self, employee):
        if employee not in self.emps:
            self.emps.append(employee)
        else:
            print("Employee already exists")
    def show_emps(self):
        for emp in self.emps:
            print(emp.fullname())

    def remove_emp(self, employee):
        if employee in self.emps:
            self.emps.remove(employee)
        else:
            print("Employee not found")

dev1 = Developer('Ahmed', 'Atef', 10000, 'Python')
dev2 = Developer('Ali', 'Alex', 20000, 'Java_Script')


manager1 = Manager('Khaled', 'Alaa', 8000, [dev1,dev2])
manager1.add_emp(dev1)

manager1.show_emps()

new_emp = Employee("Sara", "Latif", 30000)
manager2 = Manager('Mohamed', 'Shawky', 50000)

manager2.add_emp(new_emp)

manager2.show_emps()

manager2.remove_emp(dev2)


# print(isinstance(manager1, Employee))
# print(isinstance(manager1, Manager))
# print(isinstance(manager1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))