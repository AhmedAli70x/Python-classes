import datetime

class Employee():
    raiseAmount = 1.04
    empNumber = 0
    def __init__(self, first, last, salary):
        self.first= first
        self.last= last
        self.salary= salary
        self.email = first + '.' + last + '@gmail.com'

        Employee.empNumber +=1
    def fullname(self):
        return f'{self.first}  {self.last}'

    def apply_raise(self):
        self.salary = self.salary * self.raiseAmount

    @classmethod        # creating methon related to the class
    def applyRaise(cls, amount):
        cls.raiseAmount =  amount

    @classmethod
    def from_srting(cls,string):
        first, last, salary = string.split('-')
        return cls(first, last, salary)

    @staticmethod
    def work_day(day):  #day format year,month,day
        if day.weekday() == 4 or day.weekday() == 5: # Friday=4, Saturday=5
            return False
        return True

emp1 = Employee('Ahmed', 'Atef', 10000)
emp2 = Employee('Ali', 'Alex', 20000)

emp_str1 = 'Elissa-Zakaria-30000'
emp_str2 = 'Gon-Freks-50000'

newEmp1 = Employee.from_srting(emp_str1)
newEmp2 = Employee.from_srting(emp_str2)
print(newEmp1.__dict__,"\n",newEmp2.__dict__)

day = datetime.date(1994,10,27)
print(Employee.work_day(day))

