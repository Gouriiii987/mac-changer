#!/usr/bin/env python

interface=input("interface >")
new_mac=input("new_mac >")

import subprocess
subprocess.call(["ifconfig" ,interface , "down"])
subprocess.call(["ifconfig" ,interface,  "hw ether" ])
subprocess.call(["ifconfig" ,interface, "up"])
subprocess.call(["ifconfig"])

