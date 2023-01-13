#!/usr/bin/python3
import crayons

print(crayons.red('red string'))

print(f"{crayons.red('red')} white {crayons.blue('blue')}")

crayons.disable()
print(f"{crayons.red('red')} white {crayons.blue('blue')}")  # f-string (newest version of string templating)

crayons.DISABLE_COLOR = False

# This line will print in color because color is enabled
print(f"{crayons.red('red')} white {crayons.blue('blue')}")  # f-string (newest version of string templating)

# print 'red string' in red
print(crayons.red('red string', bold=True))

# print 'yellow string' in yellow
print(crayons.yellow('yellow string', bold=True))

# print 'magenta string' in magenta
print(crayons.magenta('magenta string', bold=True))

# print 'white string' in white
print(crayons.white('white string', bold=True))
