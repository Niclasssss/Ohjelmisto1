while True:
    tuumat = float(input("Enter length in inches (negative value to quit): "))
    sentit = tuumat * 2.54
    if tuumat < 0:
        print("Program ended.")
        break
    else:
        print(f"{tuumat} inches is {sentit:.2f} centimeters")