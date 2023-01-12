#!/usr/bin/env python3

with open("dnsservers.txt") as dnsfile:
    for svr in dnsfile:
        print(svr,end="")

