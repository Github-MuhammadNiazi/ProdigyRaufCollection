
from Logger.Logger import Logger

class CodeBLogger(Logger):
    def __init__(self):
        self.log_file = "codeB.log"

    def log(self, message):
        with open(self.log_file, "a") as file:
            file.write(message + "\n")
