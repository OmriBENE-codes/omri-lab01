#Lab 1
servers = []
for serverName in range(3):
    servers.append(input(f"please enter a name for the server{i+1}"))
    print(servers)


server_and_ips = {}
for server_name in servers:
 server_ip=input(f"please insert ip for the server{i+1}")
print(server_and_ips)

############################################## teacher solution
##################task 3
server_name=input("please insert server name to view its details:")
if server_name in server_and_ips:
 print(server_and_ips[server_name])
else:
 print("server name not found")

############modify server task 4
 
is_update=input("do you want to update a server? yes/no: ")
 
if is_update == "yes":
 server_name=input("please insert server name: ")
new_ip=input("please enter the new ip")
 
if server_name in server_and_ips:
    server_and_ips[server_name] = new_ip
else:
        print("server name not found")

##################################lab2###########################
#task1

status = input("Enter the server status (running, stopped, or error): ")
if status == "running":
   print("The server is running")
elif status == "stopped":
   print("the server is down, please reset")
elif status == "error":
   print("theres an error, immidiet help is requierd! ")
else:
   print("wrong statment")

#task2

servers = ["server1" , "server2" , "server3"]
for server in servers:
   print(f"pinging server {server}")

servers = {
   "server1" : "running",
   "server2" : "error",
   "server3" : "stopped"
   }
for server in servers:
    if servers[server] == "running":
      print("Healthy")
    elif servers[server] == "error":
      print("restart needed")
    elif servers[server] == "stopped":
      print("stopped")

user_input = " "
while True:
    user_input = input("Enter the server name to ping (or type 'exit' to quit): ")
    if user_input.lower() == "exit": # Check if the user wants to exit the loop
        print("Exiting the ping program.")
        break
print(f"Pinging {user_input}... Ping successful.")