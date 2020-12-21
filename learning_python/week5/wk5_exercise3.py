import re


def normalize_mac(mac_address):

    mac_address = mac_address.upper()

    if ":" in mac_address or "-" in mac_address:
        new_mac = []
        octets = re.split(r"[-:]", mac_address)

        for octet in octets:
            if len(octet) < 2:
                octet = octet.zfill(2)
            new_mac.append(octet)

    elif "." in mac_address:
        new_mac = []
        sections = mac_address.split(".")
        if len(sections) != 3:
            raise ValueError("Doesn't Work, Sir!")
        
        for word in sections:
            if len(word) < 4:
                new_mac.append(word[:2])
                new_mac.append(word[2:])
        
    return ":".join(new_mac)

print(normalize_mac('123.234.456'))
print(normalize_mac('aabb.ccdd.eeff'))
print(normalize_mac('a:b:c:d:e:f'))
print(normalize_mac('1:2:a:b:3:44'))
print(normalize_mac('a-b-c-d-e-f'))
print(normalize_mac('1-2-a-b-3-44'))
print("Tests passed")