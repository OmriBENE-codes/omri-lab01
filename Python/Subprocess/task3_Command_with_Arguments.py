#Run Command with Arguments 
import subprocess

command = input('Enter text to echo: ')
result = subprocess.run(['echo', command], capture_output=True, text= True)

print(f'\nOutput from the echo command is: \n {result.stdout}')

"""
This script captures that printed text and displays it through Python, 
allowing you to manipulate or store the output if needed.
"""