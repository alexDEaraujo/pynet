import random

def gen_ip(network="10.10.10."):
    octet4 = str(random.randint(1, 254))
    return network + octet4


print()
print(gen_ip())
print(gen_ip("192.168.168."))
print(gen_ip(network="172.16.8."))
print()