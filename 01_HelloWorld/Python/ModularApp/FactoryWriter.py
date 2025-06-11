from ClassWriter import CodeAWriter,CodeBWriter
def getInstance786(x):
    if x=="CodeAWriter":
        return CodeAWriter()
    elif x=="CodeBWriter":
        return CodeBWriter()
    else:
        print("You are makng incorrect choice!")
        return None
