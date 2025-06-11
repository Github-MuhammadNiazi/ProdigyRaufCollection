class Processor:
    def process(self,filename):
        pass
class CodeAProcessor(Processor):
    def process(self,filename):
        try:
            tuple=[]
            # with open(filename,"r") as file,open("filename786","w") as file786:
            for line in filename:
                lineWork=line.lower()
                print(lineWork)
                # file786.write(lineWork)
                tuple.append(lineWork)
            return tuple
        except Exception as e:
            print("You are having a error",e)

class CodeBProcessor(Processor):
    def process(self,filename):
        try:
            tuple=[]
            for line in filename:
                line=line[::-1]
                print(line)
                tuple.append(line)
            # with open(filename,"r") as file,open("filename786","w") as file786:
            #     for line in file:
            #         line=line[::-1]
            #         print(line,end="")
                    # file786.write(line)
                    # tuple.append(line)
            return tuple
        except Exception as e:
            print("You are having a error",e)
