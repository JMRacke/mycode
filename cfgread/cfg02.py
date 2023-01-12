#!/usr/bin/python3

configfile = open("vlanconfig.cfg")

configblog = configfile.read()

configlist = configblog.splitlines()

print(configlist)

configfile.close()


