#Deleting a File
import os
def del_file():
    file_path = input('enter the path of the file you want to delete: ')
    
    if os.path.isfile(file_path):
        confirm = (input(f'Are you sure you want to delete {file_path}? (yes/no) '))
        
        if confirm == "yes":
            os.remove(file_path)
            print(f'{file_path} has been deleted. ')
        else:
            print('The deletion is aborted.')
    else:
        print('The file does not exists.')

del_file()

