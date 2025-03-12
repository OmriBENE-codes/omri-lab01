
# file = open("server.log", "a")
# file.write("INFO: nginx started successfully. WARNING: High memory usage detected. ERROR: Disk space critical.")
error_counter = 0
with open('server.log', 'r') as file:
   for lines in file:
      if lines.startswith("ERROR"):
        error_counter += 1
      print(lines.strip())
print(f'Errors: {error_counter}')




