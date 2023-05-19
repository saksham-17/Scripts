#!/usr/bin/env Python

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its mack address")
parser.add_option("-m", "--mac_address", dest="address", help="New mac address")

(options, arguments) = parser.parse_args()
interface = options.interface
address = options.address
print("\n[+] Changing mac address for " + interface + " to " + address)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", address])
subprocess.call(["ifconfig", interface, "up"])

