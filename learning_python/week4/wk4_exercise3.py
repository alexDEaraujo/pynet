import re

with open("show_version.txt") as f:
    show_ver = f.read()

match = re.search(r"^Cisco IOS Software,.* Version (.*),", show_ver, flags=re.M)
if match:
    os_version = match.group(1)

match = re.search(r"^Processor board ID (\S+)", show_ver, flags=re.M)
if match:
    serial_number = match.group(1)

match = re.search(r"^Configuration register is (\S+)", show_ver, flags=re.M)
if match:
    config_reg = match.group(1)

print()
print("{:>20}: {:15}".format("OS Version", os_version))
print("{:>20}: {:15}".format("Serial Number", serial_number))
print("{:>20}: {:15}".format("Config Register", config_reg))
print()