#subprocess shell command andautomation
import subprocess

result = subprocess.run(["ls", "."], capture_output=True, text=True)

print(result.returncode)
print(result.stderr)
print(result.stdout)
