#Redirecting Command Output to a File
import subprocess

command = "dir"

# Execute the command and capture the output

result = subprocess.run(command, shell=True, capture_output=True, text=True)
"""shell=True: Allows the command to be executed through the shell (useful for complex commands).
capture_output=True: Captures the standard output (stdout) and standard error (stderr).
text=True: Ensures the output is returned as a string"""



with open("output.text", "w") as file: # Save the output to a text file
    file.write(result.stdout)

if result.stderr:
    print("error:", result.stderr)
