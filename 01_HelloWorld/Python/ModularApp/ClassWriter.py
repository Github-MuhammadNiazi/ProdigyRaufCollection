import os

class Writer:
    def write(self,y):
        pass
class CodeAWriter:
    def write(self,y):
        try:
            filename="good.txt"
            with open(filename, "w") as filenamer:
                for i in range(0,len(y)):
                        filenamer.write(y[i]+"\n")
            return "Here is the path of the crated .txt fle",os.path.abspath(filename)
        except Exception as e:
            print("You are having a error",e)
            return None

class CodeBWriter:
    def write(self,y):
        try:
            filename="good11.csv"
            with open(filename, "w") as filenamer:
                for  i in range(0,len(y)):

                    filenamer.write(y[i]+"\n")
            return "Here is the path of the new crated ,csv file ",os.path.abspath(filename)
        except Exception as e:
            print("You are having a error",e)
            return None

