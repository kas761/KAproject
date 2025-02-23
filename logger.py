import datetime

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file
    def log(self, log_text):
        with open(self.log_file, "a") as log:
            log.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {log_text}\n")
            print(log_text)