
from Processor.Processor import Processor

class CodeBProcessor(Processor):
    def __init__(self, logger=None):
        self.logger = logger

    def process(self, data):
        if self.logger:
            self.logger.log("CodeBProcessor: Starting processing")
        result = [line[::-1] for line in data]
        if self.logger:
            self.logger.log("CodeBProcessor: Processing completed")
        return result
