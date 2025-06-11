from FactoryReader import getInstance
from FactoryProcessor import getInstance1
from FactoryWriter import getInstance786
def main():
    choice="Enter your choce \nCodeAReader\nCodeBReader"
    patha=input(print("Enter file path"))
    patha.replace("\\", "\\\\")
    try:
        rauf =getInstance(choice)
        path=rauf.Read(patha)
        choice2="Enter your choce \nCodeAProcessor\nCodeBProcessor"
        rauf1=getInstance1(choice2)
        rauf2=rauf1.process(path)
        choice3="Entwr your choice \nCodeAWriter\nCodeBWriter"
        rauf3=getInstance786(choice3)
        print(rauf3.write(rauf2))
    except Exception as e:
        print("You are having a error",e)
if __name__ == "__main__":
    main()
