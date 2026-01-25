koko = float(input("Enter the length of the zander in centimeters: "))
puuttuvat_sentit = round(42 - koko,1)
if koko < 42:
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print("The fish was " + str(puuttuvat_sentit) + " centimeters below the size limit.")
if koko >= 42:
    print("The zander meets the size limit.")