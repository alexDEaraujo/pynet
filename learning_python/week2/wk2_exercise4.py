
with open("show_ip_int_brief.txt") as f:
    show_ip_int_brief = f.readlines()

# grab line (statically) associated with FastEthernet4
fa4_ip = show_ip_int_brief[5].strip()

# split objects from that line into a list
fields = fa4_ip.split()
intf = fields[0]
ip_address = fields[1]

# create a two element tuple
my_tuple = (intf, ip_address)
print(my_tuple)