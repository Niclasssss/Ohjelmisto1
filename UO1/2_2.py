#Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.

import math

säde = int(input("Anna ympyrän säde: "))
A = säde * säde * math.pi
print(A)