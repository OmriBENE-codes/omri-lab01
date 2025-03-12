server_metrics = {"server1" : [50,70] , 
                  "server2" : [32,67] ,
                  "server3": [80, 55] }


def analyze_server(server_name, metrics):
    metrics_amount = len(metrics)
    print(f"the length of metrics is: {metrics_amount}")
    total_sum = sum(metrics)
    print(f"The total usage is: {total_sum}")
    print(type(metrics))
    average_usage = sum(metrics)/2
    return average_usage

def check_overutilized(servers, threshold=80):
    overutilized_servers = []
    for server_name in server_metrics.keys():
        metrics = servers[server_name]
        average_usage = analyze_server(server_name, metrics)

        if metrics > threshold:
            print("avg exceeds threshold.")
            overutilized_servers.append(server_name)
    return overutilized_servers

def generate_report(servers):
    total_cpu = 0
    total_memory = 0
    for metrics in servers.values():

       
        total_cpu += metrics[0]
        total_memory += metrics[1]
    print(f"number of servers being monitored is: {len(servers)}")
    print(f"total cpu usage is: {total_cpu}")
    print(f"total memory usage is: {total_memory}")
    print(f"The average cpu usage is: {total_cpu/len(servers)}")
    print(f"The average memory usage is: {total_memory/len(servers)}")


print(analyze_server("server2", server_metrics["server2"]))
generate_report(server_metrics)
