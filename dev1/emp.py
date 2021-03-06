import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
LOG_FORMAT = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')
file_handler = logging.FileHandler('emp.log', 'w')
file_handler.setFormatter(LOG_FORMAT)
logger.addHandler(file_handler)

class Employee:

    # class variables
    num_of_emps = 0
    raise_amount = 1.04

    # class constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@intel.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return F'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    # Introducing dunder methods to avoid class printing objects
    # It give us the opportunity to decide how we want our object to be printed.
    # when you don't call them the right way.

    def __repr__(self):
        return F"Employee({self.first}, {self.last}, {self.pay})"

    def __str__(self):
        return F"{self.fullname} - {self.pay} ."

    def __len__(self):
        return len(self.fullname)

    def __add__(self, other):
        return self.pay + other.pay

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        """
        With setters we can modify fullname without issues
        :param name:
        :return:
        """
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name')
        self.first = None
        self.last = None


emp_1 = Employee('Aji', 'Jaw', 50000)
emp_2 = Employee('Aisha', 'Jaw', 750000)
emp_3 = 'Salem-Jaw-690000'

# print(Employee.fullname(emp_1))
new_emp = Employee.from_string(emp_3)
# print(new_emp.fullname())
# print(new_emp.email)
# print(Employee.num_of_emps)
# emp_1.fullname = "Modou Jaw"
# print(emp_1.first)

logger.info(str(emp_1))
# This is the same as
logger.info(emp_1.__str__())



import datetime
check_is_work = datetime.date(2019, 11, 19)

# print(Employee.is_workday(check_is_work))
# print(emp_1.fullname())
# print(emp_2.__str__())
