#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan
#Käytä for-toistorakennetta.

import random

lista = []

lkm = int(input("Anna arpakuutioiden lukumäärä: "))

for i in range(lkm):
    h = random.randint(1, 6)
    lista.append(h)

print("Heitot", lista)
print("Summa: ", sum(lista))