from pprint import pprint

with open("show_arp.txt") as f:
    show_arp = f.read()

found1, found2 = (False, False)
for line in show_arp.splitlines():
    if "protocol" in line.lower():
        continue
    fields = line.split()
    ip_addr = fields[1]
    mac_addr = fields[3]
    if ip_addr == "10.220.88.1":
        print("Default gateway IP/MAC:\t{}/{}".format(ip_addr, mac_addr))
        found1 = True
    elif ip_addr == "10.220.88.30":
        print("Arista3 IP/MAC:\t\t{}/{}".format(ip_addr, mac_addr))
        found2 = True
    
    if found1 and found2:
        print("Got 'em!")
        break

print()