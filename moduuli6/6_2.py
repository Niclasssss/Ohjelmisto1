import random

def roll_dice(maksimi):
    while True:
        luku = random.randint(1, maksimi)
        print(luku)
        if luku == maksimiluku:
            break

maksimiluku = int(input("Anna maksimisilmäluku: "))

if maksimiluku >= 2:
    roll_dice(maksimiluku)
else:
    print("Anna isompi luku.")