import random

heitot = int(input("How many dices to roll: "))
summa = 0

for i in range(heitot):
    heitto = random.randint(1,6)
    summa += heitto

print("Sum of the dice:", summa)