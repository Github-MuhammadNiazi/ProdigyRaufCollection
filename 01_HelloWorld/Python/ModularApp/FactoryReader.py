from ClassReader import CodeAReader,CodeBReader
def getInstance(x):
    if x=="CodeAReader":
        print("We have entered the codeAReader")
        return CodeAReader()
    elif x=="CodeBReader":
        print("We have entered the codeBReader")
        return CodeBReader()
    else:
        print("I don't recognize the codeAReader")
        return "bad"
