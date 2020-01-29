import re

with open("show_ipv6_intf.txt") as f:
    show_intf = f.read()

# match = re.search(r"IPv6 address:.*\s(\S+) \[VALID\].* (\S+).*IPv6 subnet:", show_intf, flags=re.DOTALL)
match = re.search(r"IPv6 address:\s(.*)\s+IPv6 subnet:", show_intf, flags=re.DOTALL)

ipv6_addresses = match.group(1).strip()
ipv6_list = ipv6_addresses.splitlines()

for i, address in enumerate(ipv6_list[:]):
    address = re.sub(r"\[VALID\]", "", address)
    ipv6_list[i] = address.strip()

print(match.group(1).strip())
print(ipv6_addresses)

print("-" * 60)
print(ipv6_list)
print("-" * 60)