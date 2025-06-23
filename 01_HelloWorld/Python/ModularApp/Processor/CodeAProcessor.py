
from Processor.Processor import Processor

class CodeAProcessor(Processor):
    def __init__(self, logger=None):
        self.logger = logger

    def process(self, data):
        
        self.logger.log("CodeAProcessor: Starting processing")
        result = [line.lower() for line in data]
        
        self.logger.log("CodeAProcessor: Processing completed")
        return result
