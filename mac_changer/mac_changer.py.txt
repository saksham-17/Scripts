#!/usr/bin/env Python

import subprocess

interface = input("network interface> ")
address = input("mac address> ")
print("[+] Changing mac address for " + interface + " to " + address)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", address])
subprocess.call(["ifconfig", interface, "up"])
subprocess.call(["ifconfig", interface])
