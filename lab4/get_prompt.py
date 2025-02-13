# from netmiko import Netmiko
# device = {
# "device_type": "cisco_ios",
# "ip": "192.168.1.101", # R1 Mgmt Interface
# "username": "student",
# "password": "Meilab123",
# "port": "22",
# }
# net_connect = Netmiko(**device)
# print(net_connect)
# from netmiko import Netmiko
# device = {
# "device_type": "cisco_ios",
# "ip": "192.168.1.101", # Router 1
# "username": "student",
# "password": "Meilab123",
# "secret": "cisco",
# "port": "22",
# }
# net_connect = Netmiko(**device)
# print(f"Default prompt: {net_connect.find_prompt()}")
# net_connect.send_command_timing("disable")
# print(f"Disable command: {net_connect.find_prompt()}")
# net_connect.enable()
# print(f"Enable command: {net_connect.find_prompt()}")
from netmiko import Netmiko

# List of device IPs to iterate over
device_ips = ["192.168.1.102", "192.168.1.103", "192.168.1.104"]

# Loop over each device IP
for ip in device_ips:
    device = {
        "device_type": "cisco_ios",
        "ip": ip,
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    }
    net_connect = Netmiko(**device)

    print(f"Default prompt for {ip}: {net_connect.find_prompt()}")

    net_connect.send_command_timing("disable")
    print(f"Prompt after 'disable' command for {ip}: {net_connect.find_prompt()}")

    net_connect.enable()
    print(f"Prompt after entering enable mode for {ip}: {net_connect.find_prompt()}")

    net_connect.disconnect()

