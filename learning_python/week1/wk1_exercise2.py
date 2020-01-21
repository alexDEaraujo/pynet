from __future__ import print_function

try:
    # Python2
    ip_addr1 = raw_input("Please Enter an IP Address: ")
except NameError:
    # Python3
    ip_addr1 = input("Please Enter an IP Address: ")

octets = ip_addr1.split(".")
dotted_line = "-" * 60

print()
print("{:^15}{:^15}{:^15}{:^15}".format("Octet1", "Octet2", "Octet3", "Octet4"))
print(dotted_line)
print("{:^15}{:^15}{:^15}{:^15}".format(octets[0], octets[1], octets[2], octets[3]))
print("{:^15}{:^15}{:^15}{:^15}".format(bin(int(octets[0])), bin(int(octets[1])),
                                        bin(int(octets[2])), bin(int(octets[3]))))
print("{:^15}{:^15}{:^15}{:^15}".format(hex(int(octets[0])), hex(int(octets[1])),
                                        hex(int(octets[2])), hex(int(octets[3]))))
print(dotted_line)