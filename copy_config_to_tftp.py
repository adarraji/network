#!/usr/bin/env python

"""
Author: Ali Darraji
Purpose: Copy running config from list of Arista and Cisco switches to TFTP server .
"""

from netmiko import ConnectHandler
from getpass import getpass
import time
from pprint import pprint as pp


admin_user = "admin"
admin_password = getpass(prompt="admin passowrd ?")

devices = [
    {
        "device_type": "arista_eos",
        "ip": "10.6.23.11",
        "host": "switch-01",
        "username": admin_user,
        "password": admin_password,
        "session_log": "switch-01.txt",
    },
    {
        "device_type": "arista_eos",
        "ip": "10.6.23.12",
        "host": "switch-02",
        "username": admin_user,
        "password": admin_password,
        "session_log": "switch-02.txt",
    },
    {
        "device_type": "cisco_ios",
        "ip": "10.6.23.13",
        "host": "switch-03",
        "username": admin_user,
        "password": admin_password,
        "session_log": "switch-03.txt",
    },
    {
        "device_type": "cisco_ios",
        "ip": "10.6.23.13",
        "host": "switch-04",
        "username": admin_user,
        "password": admin_password,
        "session_log": "switch-04.txt",
    },
]


def main():

    for device in devices:
        copy_cmd = "copy running-config tftp://" + "10.1.10.90/" + device["host"]

        net_connect = ConnectHandler(**device)
        net_connect.enable()
        time.sleep(1)

        net_connect.send_command_timing(copy_cmd)
        net_connect.send_command_timing("\n")

        time.sleep(1)

        net_connect.disconnect()


if __name__ == "__main__":
    main()
