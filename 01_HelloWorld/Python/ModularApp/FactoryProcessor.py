from ClassProcessor import CodeAProcessor,CodeBProcessor
def getInstance1(choice):
    if choice=="CodeBProcessor":
        return CodeBProcessor()
    elif choice=="CodeAProcessor":
        return CodeAProcessor()
    else:
        return None
