names = set()

while True:
    name = input("Anna nimi: ")
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nAnnetut nimet: ")
for name in names:
    print(name)