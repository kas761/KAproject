class Logger:
    def __init__(self):
        self.log_file = "process_log.txt"

    def log(self, log_text):
        with open(self.log_file, "a") as log:
            log.write(log_text + "\n")
            print(log_text)