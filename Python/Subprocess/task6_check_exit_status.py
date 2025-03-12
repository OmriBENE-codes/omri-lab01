#Checking Command Exit Status
import subprocess

command = ["ls" , "-l"]

result = subprocess.run(command, capture_output=True, text=True)

# Check if the command completed successfully
if result.returncode == 0:
    print('Command executed successfully!')
    print('output:', result.stdout)
else:
    print('command failed ', result.returncode)
    print('Error: ', result.stderrt)
