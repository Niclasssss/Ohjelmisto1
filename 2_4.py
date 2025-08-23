#Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

k1 = float(input("Anna ensimmäinen kokonaisluku: "))
k2= float(input("Anna toinen kokonaisluku: "))
k3 = float(input("Anna kolmas kokonaisluku: "))
summa = k1 + k2 + k3
tulo = k1 * k2 * k3
keskiarvo = (k1 + k2 + k3) / 3
print("Summa on", summa)
print("Tulo on", tulo)
print("keskiarvo on", keskiarvo)