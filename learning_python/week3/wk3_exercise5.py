import os
WINDOWS = True

base_ip = "10.142.86."
base_cmd_linux = "ping -c 2"
base_cmd_win = "ping -n 2"

base_cmd = base_cmd_win if WINDOWS else base_cmd_linux

ip_list = []

for last_octet in range(1, 255):
    new_ip = base_ip + str(last_octet)
    ip_list.append(new_ip)

for i, ip_addr in enumerate(ip_list):
    print("{} ---> {}".format(i, ip_addr))

ip_list = ip_list[84:86]

print()
print("-" * 80)
for ip_addr in ip_list:
    print("IP Addr: ", ip_addr)
    return_code = os.system("{} {}".format(base_cmd, ip_addr))
    print("-" * 80)
print("-" * 80)
print()