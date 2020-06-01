import logging

""" ------------- Class to handle logging ---------------"""

class StdoutLogger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.LOG_FORMAT = logging.Formatter('%(levelname)s : %(asctime)s : %(message)s')
        self.file_handler = logging.FileHandler('employee.log', 'w')
        self.file_handler.setFormatter(self.LOG_FORMAT)
        self.logger.addHandler(self.file_handler)
#logging.basicConfig(filename='employee.log', level=logging.INFO, format=LOG_FORMAT, filemode='w')


