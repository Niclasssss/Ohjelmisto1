#Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.

import math

s = input("Anna ympyrän säde: ")
r = float(s)
A = math.pi * (r*r)
print(A)