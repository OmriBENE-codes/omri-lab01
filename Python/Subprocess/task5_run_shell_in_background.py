#Running a Command in the Background
import subprocess

process = subprocess.Popen(["ping","google.com"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print("Process has been launched.")

# Optionally, you can get the process's output later:
stdout, stderr = process.communicate()

# Print the output after the process finishes
print("Process output:", stdout.decode())
if stderr:
    print("Process errors:", stderr.decode())

