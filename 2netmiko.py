from netmiko import ConnectHandler

cisco1 = {
    "device_type": "cisco_xr",
    "host": "10.10.20.173",
    "username": "cisco",
    "password": "cisco"
}

connection = ConnectHandler(**cisco1)

cmd1 = "scp de@9.3.251.51:/disk0:/file1 /disk0:/."
output = connection.send_command_timing(cmd1)
if 'Password:' in output:
    output += connection.send_command_timing("cisco")
print(output)

print("Closing connection")
connection.disconnect()