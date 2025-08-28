#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
#Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
#Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
#Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

arvaus = int(input("Arvaa lukema: "))
arpa = random.randint(1, 10)
while arvaus < arpa:
    print("Liian pieni")
    arvaus = int(input("Arvaa lukema: "))

while arvaus > arpa:
    print("Liian iso")
    arvaus = int(input("Arvaa lukema: "))

while arvaus == arpa:
    print("Oikein")
    break