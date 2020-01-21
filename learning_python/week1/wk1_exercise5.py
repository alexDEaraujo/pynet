from __future__ import print_function, unicode_literals

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"
line = "-" * 20

list1 = mac1.split()
list2 = mac2.split()
list3 = mac3.split()

print()
print("{:^20} {:^20}".format("IP ADDR", "MAC ADDR"))
print("{:>20} {:>20}".format(line, line))
print("{:>20} {:>20}".format(list1[1], list1[3]))
print("{:>20} {:>20}".format(list2[1], list2[3]))
print("{:>20} {:>20}".format(list3[1], list3[3]))