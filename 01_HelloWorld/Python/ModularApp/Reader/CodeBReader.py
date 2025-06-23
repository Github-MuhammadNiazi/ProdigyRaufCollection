
from Reader.Reader import Reader
import csv

class CodeBReader(Reader):
    def __init__(self, logger=None):
        self.logger = logger

    def read(self, filepath):
        if self.logger:
            self.logger.log(f"CodeBReader: Reading from {filepath}")
        with open(filepath, newline='') as csvfile:
            data = [",".join(row) for row in csv.reader(csvfile)]
        if self.logger:
            self.logger.log(f"CodeBReader: Successfully read {len(data)} rows")
        return data
