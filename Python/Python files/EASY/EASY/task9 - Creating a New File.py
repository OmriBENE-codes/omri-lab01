#Creating a New File

def create_file():
    file_name = input('Enter The name of the file (e.g "example.txt"): ')
    content = """
Here is a new file being birthed at the of the task.
should it stay or shoud it go?
"""
    with open(file_name, "w") as file:
         file.write(content) #writes into a file content, input or else.
    print(f' {file_name} has been created with default content.')

create_file()
