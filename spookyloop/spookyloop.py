#!/usr/bin/python3

linecount = 0

with open('dracula.txt','r') as dracula:
    with open('vampytimes.txt','w') as vamps:
        for line in dracula.readlines():
            if 'vampire' in line.lower():
                print(line.strip())
                print(line.strip() , file=vamps)
                linecount += 1

print(f"{linecount} {'lines' if linecount != 1 else 'line'} contain the word vampire!")


