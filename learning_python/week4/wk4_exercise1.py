
device = {
    "ip_addr" : "192.168.9.1",
    "vendor" : "cisco",
    "username" : "my_username",
    "password" : "password123"
}

bgp_fields = {
    "bgp_as" : "65664",
    "peer_as" : "21580",
    "peer_ip" : "10.2.45.6"
}

banner = "-" * 40
print(banner)
print(device["ip_addr"])
print(banner)

if device["vendor"].lower() == "cisco":
    device["platform"] = "ios"
elif device["vendor"].lower() == "juniper":
    device["platform"] = "junos"

device.update(bgp_fields)

print()
print(banner)
for key in device:
    print("{:>15}".format(key))
print(banner)
print()

print(banner)
for key, value in device.items():
    print("{key:>15} ---> {value:>15}".format(key=key, value=value))
print(banner)
print()