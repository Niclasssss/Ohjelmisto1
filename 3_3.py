#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
#Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

s = input("Anna sukupuolesi: ")
h = int(input("Anna hemoglobiiniarvosi: "))

if s == "Nainen" and h <= 117:
    print("Hemoglobiiniarvosi on alhainen")
elif s == "Nainen" and h >= 117 and h <= 175:
    print("Hemoglobiiniarvosi on normaali")
elif s == "Nainen" and h >= 175:
    print("Hemoglobiinisi on korkea")

elif s == "Mies" and h <= 134:
    print("Hemoglobiiniarvosi on alhainen")
elif s == "Mies" and h >= 134 and h <= 195:
    print("Hemoglobiiniarvosi on normaali")
elif s == "Mies" and h >= 195:
    print("Hemoglobiinisi on korkea")
else:
    print("Väärät tiedot")