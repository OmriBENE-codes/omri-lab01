#Running a Simple Shell Command
import subprocess
import os

# Determine the command based on the OS
if os.name == 'nt': # For Windows
    command = 'dir'
else:
    command = 'ls'  # For Linux/macOS

result = subprocess.run(command, capture_output= True, text= True, shell=True)

print('command output: ')
print(result.stdout)

if result.stderr:
    print("Error:")
    print(result.stderr)


