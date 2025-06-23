
from Writer.CodeAWriter import CodeAWriter
from Writer.CodeBWriter import CodeBWriter

def get_writer_instance(code_type, logger):
    if code_type == "A":
        return CodeAWriter(logger)
    elif code_type == "B":
        return CodeBWriter(logger)
    else:
        raise ValueError("Invalid code type")
