from netmiko import ConnectHandler

cisco1 = {
    "device_type": "cisco_xr",
    "host": "10.10.20.173",
    "username": "cisco",
    "password": "cisco"
}

connection = ConnectHandler(**cisco1)

output=connection.send_command("sh ipv4 int brief")
print(output)

print("Closing connection")
connection.disconnect()