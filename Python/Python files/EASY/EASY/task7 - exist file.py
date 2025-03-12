#Checking If a File Exists

import os.path

path = './example.txt'
check_file = os.path.isfile(path)
print(f'file exists : {check_file} ')