#Reading from a File

def read_file():
    open_file = open('example.txt', "r")
    content = open_file.read()
    print(content)

read_file()