#Capturing Command Output
import subprocess

# Run the 'dir' command on Windows and capture the output
result = subprocess.run(['cmd', '/c', 'dir'], capture_output=True, text=True)

output = result.stdout #store the output in a variable

print(output) #store the output
