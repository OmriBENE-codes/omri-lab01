#Copying File Contents 
import shutil #lets you manipulate files and directories and perform file and directory operations
def copy_file():
    path = './example.txt' #where is the file to copy
    destination = ".\exampleCopy.txt" #new file to make
    shutil.copy(path , destination) 

"""
copy2 --> preserves the original file metadata when copying
#copyfileobj ---> Keep in mind that this method does not 
               preserve file permissions and it doesn't copy metadata
"""
