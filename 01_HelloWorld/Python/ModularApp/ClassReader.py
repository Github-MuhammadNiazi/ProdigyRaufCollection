


class Reader:
    def Read(self,zz):
        pass
class CodeAReader(Reader):

    def Read(self,zz):
        if zz.endswith(".txt"):
            try:
                tuple=[]
                with open(zz, 'r') as file:
                    for line in file:
                        print(line.strip())
                        tuple.append(line.strip())
                    return tuple
            except FileNotFoundError:
                print("File not found")
            except Exception as e:
                print("Something went wrong",e)
                return None
        else:
            print("File type not supported")
            return None
class CodeBReader(Reader):
    def Read(self,zz):
        if zz.endswith(".csv"):
            try:
                tuple=[]
                with open(zz,"r") as file:
                    for line in file:
                        print(line.strip())
                        tuple.append(line.strip())

                    return tuple
            except Exception as e:
                print("Something went wrong",e)
                return None
            print("I am the CodeBReader")
            print("The additional argument is :" + zz)
            return "You are a nice guy using CodeBReader"
        else:
            print("File type not supported")
