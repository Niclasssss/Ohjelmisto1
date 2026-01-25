sukupuoli = input("Enter biological gender (male/female): ").lower()
hemoglobiini = float(input("Enter hemoglobin value (g/l): "))

if sukupuoli == "female":
    if 117 <= hemoglobiini <= 155:
        print("Your hemoglobin is normal.")
    elif hemoglobiini < 117:
        print("Your hemoglobin is low.")
    else:
        print("Your hemoglobin is high.")

elif sukupuoli == "male":
    if 134 <= hemoglobiini <= 167:
        print("Your hemoglobin is normal.")
    elif hemoglobiini < 134:
        print("Your hemoglobin is low.")
    else:
        print("Your hemoglobin is high.")
else:
    print("Invalid gender.")