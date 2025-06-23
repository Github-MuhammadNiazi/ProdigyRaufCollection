
from Writer.Writer import Writer

class CodeAWriter(Writer):
    def __init__(self, logger=None):
        self.logger = logger

    def write(self, filepath, data):
        if self.logger:
            self.logger.log(f"CodeAWriter: Writing to {filepath}")
        with open(filepath, 'w') as file:
            file.writelines(data)
        if self.logger:
            self.logger.log("CodeAWriter: Write completed")
