server_name = input("Enter server name: ")

try:
        if not server_name:
         raise ValueError("server name is empty.")
    
        if not server_name.isalnum():
                raise ValueError("server name is not alphanumeric.")


except ValueError as e:
     print(f"Error: {e}")

if server_name in ["docker", "ngnix"]:
    print("server is running. ")
else:
    print("server is not running.")