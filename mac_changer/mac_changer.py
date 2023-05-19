#!/usr/bin/env Python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its mack address")
    parser.add_option("-m", "--mac_address", dest="address", help="New mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please enter the interface, use --help for more info ")
    elif not options.address:
        parser.error("[-] Please enter the mac address, use --help for more info ")
    return options

def change_mac(interface,address):
    print("\n[+] Changing mac address for " + interface + " to " + address)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", address])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.address)




