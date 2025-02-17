import datetime
import requests

class DataRetrieval:
    def __init__(self, data_file, data_type, url, processor, logger):
        self.data_file = data_file
        self.data_type = data_type
        self.url = url
        self.logger = logger
        self.processor = processor

    def retrieve_data(self):
        self.logger.log(f"Task started at {datetime.datetime.now()}")
        response = requests.get(self.url)
        if response.status_code == 200:
            retrieved_data = response.json()
            with open(self.data_file, "r") as file_read:
                content = file_read.read()
        return content, retrieved_data
                    
    def write_data(self, content, retrieved_data):
        new_lines = 0
        repeats = 0
        with open(self.data_file, "a") as file_write:
            for data_item in retrieved_data:
                if str(data_item) not in content:
                    file_write.write(f"{data_item}\n")
                    new_lines += 1
                else:
                    repeats += 1
        self.logger.log(f"Added {new_lines} new lines and {repeats} repeats occurred")