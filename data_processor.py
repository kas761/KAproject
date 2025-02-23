"""
Module for processing data from a file and logging the results.
"""

import os

class DataProcessor:
    """Class to process data from a file."""

    def __init__(self, data_file, logger):
        """
        Initialize the DataProcessor with a data file and a logger.

        :param data_file: Path to the data file.
        :param logger: Logger instance for logging messages.
        """
        self.data_file = data_file
        self.logger = logger

    def read_file(self):
        """
        Read the data file and log the number of lines and characters.

        Logs an error if the file does not exist or is empty.
        """
        try:
            if not os.path.exists(self.data_file):
                self.logger.log(f"Error: The file {self.data_file} does not exist.")
                return
            with open(self.data_file, 'r', encoding='utf-8') as file:
                content = file.read()
                if not content:
                    self.logger.log(f"Error: The file {self.data_file} is empty.")
                    return
                line_count = content.count('\n') + 1
                char_count = len(content)
            self.logger.log(f"No of lines {line_count} and characters {char_count} in the file")
        except OSError as e:
            self.logger.log(f"An error occurred while reading the file: {str(e)}")
        finally:
            self.logger.log("Task finished. File read completed.")
