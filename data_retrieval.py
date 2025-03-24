import os
import requests

class DataRetrieval:
    def __init__(self, data_file, data_type, url, logger, processor):
        self.data_file = data_file
        self.data_type = data_type
        self.url = url
        self.logger = logger
        self.processor = processor

    def retrieve_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                content = file.read()
        else:
            self.logger.log(f"File {self.data_file} does not exist. Proceeding with empty content.")
            content = ""

        try:
            response = requests.get(self.url)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            self.logger.log(f"HTTP request failed: {e}")
            return content, []
        except ValueError as e:
            self.logger.log(f"Data validation error: {e}")
            return content, []

        return content, data
                       
    def write_data(self, content, retrieved_data):
        if content is None or retrieved_data is None:
            self.logger.log("No data to write due to previous errors")
            return
        
        new_lines = 0
        repeats = 0
        with open(self.data_file, "a", encoding='utf-8') as file_write:
            for data_item in retrieved_data:
                if str(data_item) not in content:
                    file_write.write(f"{data_item}\n")
                    new_lines += 1
                else:
                    repeats += 1
        self.logger.log(f"Added {new_lines} new lines and {repeats} repeats occurred")
