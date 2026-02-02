def get_season(kuukausi):
    if kuukausi in (12, 1, 2):
        return "winter"
    elif kuukausi in (3, 4, 5):
        return "spring"
    elif kuukausi in (6, 7, 8):
        return "summer"
    elif kuukausi in (9, 10, 11):
        return "autumn"
    else:
        return None

kuukausi = int(input("Enter the number of a month (1-12): "))
vuodenaika = get_season(kuukausi)

if vuodenaika is not None:
    print(f"You entered: {kuukausi}\nThe season is {vuodenaika}.")
else:
    print(f"You entered: {kuukausi}\nPlease enter a number between 1 and 12.")