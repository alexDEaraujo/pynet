from __future__ import print_function, unicode_literals

show_version = "*0 CISCO881-SEC-K9 FTX0000038X "
show_version = show_version.strip()
fields = show_version.split()

model = fields[1]
serial_number = fields[2]

print()
vendor_cisco = 'cisco' in model.lower()
print("Checking if model contains Cisco: {}".format(vendor_cisco))
print()

model_881 = '881' in model
print("Checking is model contains 881: {}".format(model_881))
print()

print("Serial Number: {}".format(serial_number))
print("Model: {}".format(model))
print()