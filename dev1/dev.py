from emp import Employee


class Developer(Employee):
    """It inherited everything from Employee class"""
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.p_lang = prog_lang


dev_1 = Developer('Aji AMie', 'Jaw', 50000, 'python')
# dev_2 = Developer('Aisha', 'Jaw', 750000)
# dev_3 = 'Salem-Jaw-690000'
emp_5 = Employee('Aji AMie', 'Jaw', 50000)


# print(emp_1.fullname())
# emp_4 = Employee.from_string(emp_3)
# print(emp_4.fullname())
#by changing the raise amount in developer. It doesn't have any impact on our Employee class
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
#
# print(emp_5.pay)
# emp_5.apply_raise()
# print(emp_5.pay)
#

import datetime
check_is_work = datetime.date(2021, 8, 6)
print(Developer.is_workday(check_is_work))
