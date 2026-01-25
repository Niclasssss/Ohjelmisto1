hyttiluokka = input("Enter the cabin class(LUX, A, B, or C): ")

if hyttiluokka == "LUX":
    print("Enter the cabin class (LUX, A, B, or C): Upper-deck cabin with a balcony.")
elif hyttiluokka == "A":
    print("Enter the cabin class (LUX, A, B, or C): Above the car deck, equipped with a window.")
elif hyttiluokka == "B":
    print("Enter the cabin class (LUX, A, B, or C): Windowless cabin above the car deck.")
elif hyttiluokka == "C":
    print("Enter the cabin class (LUX, A, B, or C): Windowless cabin below the car deck.")
else:
    print("Enter the cabin class(LUX, A, B, or C):  Invalid cabin class.")