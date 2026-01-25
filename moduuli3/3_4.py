vuosi = int(input("Enter a year: "))

if (vuosi % 4 == 0 and vuosi % 100 != 0) or vuosi % 400 == 0:
    print(str(vuosi) + " is a leap year.")
else:
    print(str(vuosi) + " is not a leap year.")