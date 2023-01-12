from emp import Employee
from dev import Developer
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
LOG_FORMAT = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')
file_handler = logging.FileHandler('mgr.log', 'w')
file_handler.setFormatter(LOG_FORMAT)
logger.addHandler(file_handler)

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
            message = F'-->{emp.fullname}'
            logger.info(message)


dev_1 = Developer('Aji AMie', 'Jaw', 50000, 'python')
dev_2 = Developer('Aisha', 'Jaw', 25000, 'C++')
mgr_1 = Manager('Adam', 'Silveria', 165000, [dev_1])

logger.info(mgr_1.fullname)
logger.info(mgr_1.email)
mgr_1.add_emp(dev_1)
#mgr_1.rem_emp(dev_1)

mgr_1.print_emps()

logger.info(isinstance(mgr_1, Developer))
logger.info(issubclass(Manager, Employee))
logger.info(issubclass(Manager, Developer))
