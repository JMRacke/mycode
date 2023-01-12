#!/usr/bin/python3

configfile = open("vlanconfig.cfg")

print(configfile.read())

configfile.close()


configfile = open("vlanconfig.cfg")

configlist = configfile.readlines()
print(configlist)

for x in configlist:
    x = x.strip()
    print(x)


configfile.close()

