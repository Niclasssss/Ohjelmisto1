luvut = []

luku = input("Enter a number: ")

while luku !="":
    luvut.append(float(luku))
    luku = input("Enter a number: ")

luvut.sort(reverse=True)

print("The greatest numbers in descending order: ")
for luku in luvut[:5]:
    print(luku)