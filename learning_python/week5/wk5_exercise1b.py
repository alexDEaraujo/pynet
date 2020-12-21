def ssh_conn2(ip_addr, username, password, device_type="cisco_ios"):
    print("IP {}".format(ip_addr))
    print("Username {}".format(username))
    print("Password {}".format(password))
    print("Device Type {}".format(device_type))
    print("-" * 25)
    return


# adding default values
ssh_conn2("10.1.1.1", "alex", "pass123")

ssh_conn2(username="usernamed", ip_addr="10.2.2.2",
          password="passwdnamed", device_type="junos")

# calling using a dictionary
my_device = {
    "ip_addr": "10.4.4.4",
    "username": "mydictuser",
    "password": "mydictpasswd",
    "device_type": "fortios"
}
ssh_conn2(**my_device)
