#!/usr/bin/python3
fname = input("Enter a file name: ")
with open(fname,'r') as file:
    print(file.readlines())

