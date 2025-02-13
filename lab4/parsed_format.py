# from netmiko import Netmiko
# device = {"device_type": "cisco_ios",
# "ip": "192.168.1.101",
# "username": "student",
# "password": "Meilab123",
# "port": "22"}
# net_connect = Netmiko(**device)
# output = net_connect.send_command("show ip interface brief")
# net_connect.disconnect()
# print(type(output))
# print(output)
# from netmiko import Netmiko
# device = {"device_type": "cisco_ios",
# "ip": "192.168.1.101",
# "username": "student",
# "password": "Meilab123",
# "port": "22"}
# net_connect = Netmiko(**device)
# output = net_connect.send_command("show ip interface brief", use_textfsm=True)
# net_connect.disconnect()
# print(type(output))
# for interface in output:
#     print(interface['interface'])
# from netmiko import Netmiko
# import os

# # List of routers in the topology
# routers = [
#     {"device_type": "cisco_ios", "ip": "192.168.1.101", "username": "student", "password": "Meilab123", "port": "22"},
#     {"device_type": "cisco_ios", "ip": "192.168.1.102", "username": "student", "password": "Meilab123", "port": "22"},
#     {"device_type": "cisco_ios", "ip": "192.168.1.103", "username": "student", "password": "Meilab123", "port": "22"},
#     # Add more routers if needed...
# ]

# # Function to get interfaces from a router
# def get_interfaces(device):
#     try:
#         # Connect to the router
#         net_connect = Netmiko(**device)
        
#         # Send the "show ip interface brief" command and parse it using TextFSM
#         output = net_connect.send_command("show ip interface brief", use_textfsm=True)
        
#         # Disconnect the session
#         net_connect.disconnect()
        
#         return output
    
#     except Exception as e:
#         print(f"Failed to connect to {device['ip']}: {e}")
#         return []

# # Loop through all routers and get interfaces
# all_interfaces = {}
# for device in routers:
#     print(f"Getting interfaces for {device['ip']}...")
#     interfaces = get_interfaces(device)
#     if interfaces:
#         all_interfaces[device['ip']] = interfaces

# # Print the interfaces for each router
# for ip, interfaces in all_interfaces.items():
#     print(f"Interfaces for {ip}:")
#     for interface in interfaces:
#         print(f" - {interface['interface']}")

from netmiko import Netmiko
import os

# List of routers in the topology
routers = [
    {"device_type": "cisco_ios", "ip": "192.168.1.101", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.102", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.103", "username": "student", "password": "Meilab123", "port": "22"},
    # Add more routers if needed...
]

# Function to get routing table from a router
def get_ip_route(device):
    try:
        # Connect to the router
        net_connect = Netmiko(**device)
        
        # Send the "show ip route" command and parse it using TextFSM
        output = net_connect.send_command("show ip route", use_textfsm=True)
        
        # Disconnect the session
        net_connect.disconnect()
        
        return output
    
    except Exception as e:
        print(f"Failed to connect to {device['ip']}: {e}")
        return []

# Loop through all routers and get ip route information
all_routes = {}
for device in routers:
    print(f"Getting IP route for {device['ip']}...")
    routes = get_ip_route(device)
    if routes:
        all_routes[device['ip']] = routes

# Print the parsed routing table for each router
for ip, routes in all_routes.items():
    print(f"\nIP Route for {ip}:")
    for route in routes:
        # Print the relevant details: protocol, network, distance, and metric
        protocol = route.get("protocol", "N/A")
        network = route.get("network", "N/A")
        distance = route.get("distance", "N/A")
        metric = route.get("metric", "N/A")

        print(f"Protocol: {protocol}, Network: {network}, Distance: {distance}, Metric: {metric}")

