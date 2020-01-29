houston_ips = [
    '10.10.10.1',
    '10.10.20.1',
    '10.10.30.1',
    '10.10.40.1',
    '10.10.50.1',
    '10.10.60.1',
    '10.10.70.1',
    '10.10.80.1',
    '10.10.10.1',
    '10.10.20.1',
    '10.10.70.1',
]

atlanta_ips = [
    '10.10.10.1',
    '10.10.20.1',
    '10.10.30.1',
    '10.10.140.1',
    '10.10.150.1',
    '10.10.160.1',
    '10.10.170.1',
    '10.10.180.1',
]

chicago_ips = [
    '10.10.10.1',
    '10.10.20.1',
    '10.10.140.1',
    '10.10.150.1',
    '10.10.210.1',
    '10.10.220.1',
    '10.10.230.1',
    '10.10.240.1',
]

banner = "-" * 80

houston_ips = set(houston_ips)
atlanta_ips = set(atlanta_ips)
chicago_ips = set(chicago_ips)

print(banner)
print("Duplicate IPs at Houston and Atlanta sites:\n\n{}".format(houston_ips & atlanta_ips))
print(banner)
print()
print(banner)
print("Duplicate IPs at all three sites:\n\n{}".format(houston_ips & atlanta_ips & chicago_ips))
print(banner)
print()
print(banner)
print("Unique addresses in Chicago:\n\n{}".format(chicago_ips.difference(houston_ips).difference(atlanta_ips)))
print(banner)
print()