# from __future__ import print_function

# old way of doing it
#
f = open("show_version.txt", "r")
output = f.read()
print(output)
print(type(output))
f.close()

# better way of doing it, because it automatically closes the file
#
with open("show_version.txt") as f:
    output = f.readlines()

print(output)
print(type(output))