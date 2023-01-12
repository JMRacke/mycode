#!/usr/bin/env python3

try:
    bottles = int(input("How many bottles of beer are on the wall? "))
except:
    print("that's not a number in the valid range (<100)!")
    bottles = 100

for i in range(bottles):
    current = bottles - i
    plural = 'bottles' if current != 1 else 'bottle'
    print(f"{current} {plural} of beer on the wall!\n{current} {plural} of beer on the wall! {current} {plural} of beer! You take one down, pass it around!")

