import logging

#Create and configure logger

Logger = logging.getLogger(__name__)
Logger.setLevel(logging.INFO)
LOG_FORMAT = logging.Formatter('%(levelname)s : %(asctime)s : %(message)s')
file_handler = logging.FileHandler('employee.log', 'w')
file_handler.setFormatter(LOG_FORMAT)
Logger.addHandler(file_handler)
#logging.basicConfig(filename='employee.log', level=logging.INFO, format=LOG_FORMAT, filemode='w')

class MyEmployees:
    """
    This is a class of employees to return
    Full name and emails
    """

    def __init__(self, first, last):
        self.first = first
        self.last = last

        Logger.info(F"Welcome to Qaf {self.fullname} your email is {self.email} ")

    @property
    def fullname(self):
        return F'{self.first} {self.last}'

    @property
    def email(self):
        return F"{self.first.lower()}.{self.last.lower()}@qaf.com"


emp1 = MyEmployees('Ajie Amie', 'Jaw')
emp2 = MyEmployees('Zakaria', 'Jaw')