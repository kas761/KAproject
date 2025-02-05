import argparse
import os
import sys
import datetime
import requests

data_file = "data.txt"
url = "https://jsonplaceholder.typicode.com/posts"

def log(log_text):
    log_file = "process_log.txt"
    with open(log_file, "a") as log:
        log.write(log_text)
        print(log_text)



def retrieve_data(data_file,url):
    log(f"Task started at {datetime.datetime.now()}")
    response = requests.get(url)
    if response.status_code == 200:
        new_lines = 0
        repeats = 0
        posts = response.json()
        with open(data_file, "a") as file_write:
            with open(data_file, "r") as file_read:
                content = file_read.read()
            for post in posts:
                if post["body"] not in content:
                    file_write.write(f"{post["body"]}\n")
                    new_lines += 1
                else:
                    repeats += 1
            log(f"Added {new_lines} new lines and {repeats} repeats occured")

def read_file(data_file):
    if not os.path.exists(data_file):
            log(f"Error: The file {data_file} does not exist.\n")
            return
    with open(data_file, 'r') as file:
        content = file.read()
        line_count = content.count('\n') + 1
        char_count = len(content)
    log(f"The number of lines in the file is: {line_count} and number of characters is: {char_count}")
    log(f"Task finished at {datetime.datetime.now()}")

retrieve_data(data_file,url)
read_file(data_file)