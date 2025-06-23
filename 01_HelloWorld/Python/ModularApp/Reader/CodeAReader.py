
from Reader.Reader import Reader

class CodeAReader(Reader):
    def __init__(self, logger=None):
        self.logger = logger

    def read(self, filepath):
        if self.logger:
            self.logger.log(f"CodeAReader: Reading from {filepath}")
        with open(filepath, 'r') as file:
            data = file.readlines()
        if self.logger:
            self.logger.log(f"CodeAReader: Successfully read {len(data)} lines")
        return data
