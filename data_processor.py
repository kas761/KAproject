import os

class DataProcessor:
    def __init__(self, data_file, logger):
        self.data_file = data_file
        self.logger = logger

    def read_file(self):
        content = None
        try:
            if not os.path.exists(self.data_file):
                self.logger.log("An error occurred while reading the file: File does not exist.")
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
            self.logger.log("An error occurred while reading the file:")
            self.logger.log(str(e))
        finally:
            # This is executed after the reading is done or if an exception occurred
            if content is not None:  # Ensure this is only logged if the file was processed
                self.logger.log("Task finished. File read completed.")
