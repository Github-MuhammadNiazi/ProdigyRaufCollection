
from Processor.CodeAProcessor import CodeAProcessor
from Processor.CodeBProcessor import CodeBProcessor

def get_processor_instance(code_type, logger):
    if code_type == "A":
        return CodeAProcessor(logger)
    elif code_type == "B":
        return CodeBProcessor(logger)
    else:
        raise ValueError("Invalid code type")
