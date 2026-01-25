pienin = None
suurin = None

while True:
    luku1 = input("Enter a number (or press Enter to quit): ")
    if luku1 == "":
        break
    luku = float(luku1)

    if pienin is None or luku < pienin:
        pienin = luku
    if suurin is None or luku > suurin:
        suurin = luku

print(f"Smallest number: {pienin} Largest number: {suurin}")