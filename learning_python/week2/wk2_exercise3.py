from pprint import pprint

with open("show_arp.txt") as f:
    show_arp = f.readlines()

# remove header line
show_arp = show_arp[1:]
pprint(show_arp)

# sort list
show_arp.sort()

# create a new list with first 3 lines
arp_entries = show_arp[:3]
arp_entries = "\n".join(arp_entries)

with open("arp_entries.txt", "wt") as f:
    f.write(arp_entries)