ip_addr = ["10.32.45.11", "192.168.13.96", "33.26.56.64", "216.57.71.30", "67.34.8.88"]

# use the .append() method to add to the list
ip_addr.append("1.1.1.1")

# use the .extend() method to add to the list
ip_addr.extend(["2.2.2.2", "3.3.3.3"])

# concatenate more items to the list
ip_addr = ip_addr + ["4.4.4.4", "5.5.5.5"]

# print full list
print(ip_addr)

# print first item on the list
print(ip_addr[0])

# print last item on the list
print(ip_addr[-1])

# use the .pop() method to remote the first and last IP Addresses from the list
first_ip = ip_addr.pop(0)
last_ip = ip_addr.pop()
print(ip_addr)

# update the new first IP address in the list to be "2.2.2.2"
ip_addr[0] = "2.2.2.2"
print(ip_addr)