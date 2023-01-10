#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)
ftp = "ftp"
protoa.insert(4,ftp) # inserts ftp before the index 4 into the list
print(protoa)
protoa.clear() # wipes the list clean
print(protoa) # prints an empty list
print(len(protoa)) # Should print 0 as the size of the list

numlist = [3,5,2345,345,267,823,4546,9]
print(numlist) # prints the list of numbers
numlist.sort() # sorts the list numerically
print(numlist) # should be sorted!

