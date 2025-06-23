
from Logger.Logger import Logger

class CodeALogger(Logger):
    def __init__(self):
        self.log_file = "codeA.log"

    def log(self, message):
        with open(self.log_file, "a") as file:
            file.write(message + "\n")
