from emp import Employee
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
LOG_FORMAT = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')
file_handler = logging.FileHandler('dev.log', 'w')
file_handler.setFormatter(LOG_FORMAT)
logger.addHandler(file_handler)


class Developer(Employee):
    """It inherited everything from Employee class"""
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.p_lang = prog_lang


dev_1 = Developer('Aji AMie', 'Jaw', 50000, 'python')
emp_5 = Employee('Aji AMie', 'Jaw', 50000)
logger.info(emp_5.pay)
# emp_5.apply_raise()
logger.info(emp_5.pay)

import datetime
check_is_work = datetime.date(2021, 8, 6)
logger.info(Developer.is_workday(check_is_work))
