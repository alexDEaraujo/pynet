def ssh_conn(ip_addr, username, password):
    print("IP {}".format(ip_addr))
    print("Username {}".format(username))
    print("Password {}".format(password))
    print("-" * 25)


# positional args
ssh_conn("10.1.1.1", "alex", "pass123")

# named args
ssh_conn(username="alexnamed", ip_addr="10.2.2.2", password="namedpassword")

# mixed named and positional args
ssh_conn("10.3.3.3", username="usermixed", password="passwdMixed")
