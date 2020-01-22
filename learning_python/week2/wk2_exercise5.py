from pprint import pprint

with open("show_ip_bgp_summ.txt") as f:
    bgp_summ = f.read()

bgp_summ = bgp_summ.splitlines()

# get the first and last line
first_line = bgp_summ[0]
last_line = bgp_summ[-1]

# from the first line use the string .split() method to obtain the local AS number
as_number = first_line.split()[-1]

# from the last line use the string .split() method to obtain the BGP peer IP address
bgp_peer_ip = last_line.split()[0]

print("Local AS:\t{}".format(as_number))
print("BGP Neighbor:\t{}".format(bgp_peer_ip))
