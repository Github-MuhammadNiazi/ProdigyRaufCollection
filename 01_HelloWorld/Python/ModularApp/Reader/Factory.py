
from Reader.CodeAReader import CodeAReader
from Reader.CodeBReader import CodeBReader

def get_reader_instance(code_type, logger):
    if code_type == "A":
        return CodeAReader(logger)
    elif code_type == "B":
        return CodeBReader(logger)
    else:
        raise ValueError("Invalid code type")
