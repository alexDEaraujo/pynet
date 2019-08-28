# making python2 and python3 code compatible
from __future__ import print_function, unicode_literals

try:
    ip_addr = raw_input("Enter and IP Address2: ")
except NameError:
    ip_addr = input("Enter and IP Address3: ")

print(ip_addr)