# Francis Oludhe
# Least difference

import sys

def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)

    return min(diff1, diff2, diff3)

print ()

a = int(input('First number: '))
b = int(input('Second number: '))
c = int(input('Third number: '))

print ()
print (least_difference(a, b, c))
print ()

sys.exit()
