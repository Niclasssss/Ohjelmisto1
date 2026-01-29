import random
def roll_dice():
    while True:
        luku = random.randint(1, 6)
        print(luku)
        if luku == 6:
            break

roll_dice()
