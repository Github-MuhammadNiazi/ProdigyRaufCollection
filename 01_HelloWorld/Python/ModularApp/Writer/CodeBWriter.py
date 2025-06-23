
from Writer.Writer import Writer
import csv

class CodeBWriter(Writer):
    def __init__(self, logger=None):
        self.logger = logger

    def write(self, filepath, data):
        if self.logger:
            self.logger.log(f"CodeBWriter: Writing to {filepath}")
        with open(filepath, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                writer.writerow(row.split(","))
        if self.logger:
            self.logger.log("CodeBWriter: Write completed")
