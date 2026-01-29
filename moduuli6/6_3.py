def gallons_to_liters (gallonat):
    return gallonat * 3.785

while True:
    gallonat = int(input("Enter a volume in American gallons (negative value to quit): "))
    if gallonat < 0:
        print("Program finished.")
        break
    else:
        litrat = gallons_to_liters(gallonat)
        print(f"{gallonat:.1f} American gallons is {litrat:.2f} liters.")