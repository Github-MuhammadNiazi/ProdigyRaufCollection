
from Logger.CodeALogger import CodeALogger
from Logger.CodeBLogger import CodeBLogger

def get_logger_instance(code_type):
    return CodeALogger() if code_type == "A" else CodeBLogger()
