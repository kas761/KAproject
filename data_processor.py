import os
import datetime

class DataProcessor:
    def __init__(self, data_file, logger):
        self.data_file = data_file
        self.logger = logger

    def read_file(self):
        if not os.path.exists(self.data_file):
            self.logger.log(f"Error: The file {self.data_file} does not exist.\n")
            return
        with open(self.data_file, 'r') as file:
            content = file.read()
            line_count = content.count('\n') + 1
            char_count = len(content)
        self.logger.log(f"The number of lines in the file is: {line_count} and number of characters is: {char_count}")
        self.logger.log(f"Task finished at {datetime.datetime.now()}")