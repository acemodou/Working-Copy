from emp import Employee
from dev import Developer


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Aji AMie', 'Jaw', 50000, 'python')
dev_2 = Developer('Aisha', 'Jaw', 25000, 'C++')
mgr_1 = Manager('Adam', 'Silveria', 165000, [dev_1])

print(mgr_1.fullname())
#print(mgr_1.email)
mgr_1.add_emp(dev_1)
#mgr_1.rem_emp(dev_1)

mgr_1.print_emps()

print(isinstance(mgr_1, Developer))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
