#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes
#käyttäjä antaa negatiivisen tuumamäärän
#Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuumat = int(input("Anna tuumat: "))

while tuumat > 0:
    cm = tuumat * 2.54
    print(cm)
    tuumat = int(input("Anna tuumat: "))
    if tuumat <= 0:
        break