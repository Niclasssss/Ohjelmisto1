#Kirjoita peli, jossa tietokone arpoo satunnaisen kokonaisluvun väliltä 1-10.
#Käyttäjä yrittää arvata lukua, kunnes arvaa oikein.
#Guess a number (1-10): Too high
#Guess a number (1-10): Too low
#Guess a number (1-10): Correct

import random

lukema = random.randint(0,10)

while True:
    arvaus = int(input("Arvaa lukema: "))
    if arvaus == lukema:
        print("Correct")
        break
    if arvaus < lukema:
        print("Too low")
    if arvaus > lukema:
        print("Too high")