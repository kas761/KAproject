import datetime
import requests

class DataRetrieval:
    def __init__(self, data_file, url, processor, logger):
        self.data_file = data_file
        self.url = url
        self.logger = logger
        self.processor = processor

    def retrieve_data(self):
        self.logger.log(f"Task started at {datetime.datetime.now()}")
        response = requests.get(self.url)
        if response.status_code == 200:
            new_lines = 0
            repeats = 0
            posts = response.json()
            with open(self.data_file, "a") as file_write:
                with open(self.data_file, "r") as file_read:
                    content = file_read.read()
                for post in posts:
                    if post["body"] not in content:
                        file_write.write(f"{post['body']}\n")
                        new_lines += 1
                    else:
                        repeats += 1
                self.logger.log(f"Added {new_lines} new lines and {repeats} repeats occurred")
