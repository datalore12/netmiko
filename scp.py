import os
from netmiko import ConnectHandler, file_transfer


cisco = {
    "device_type": "cisco_xr",
    "host": "10.10.20.173",
    "username": "cisco",
    "password": "cisco"
}

