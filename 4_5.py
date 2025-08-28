#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
#Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
#Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
#Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

kä = ("python")
sa = ("rules")

y = 0

while y <= 5:
    y1 = input("Anna käyttäjätunnus: ")
    y2 = input("Anna salasana: ")
    if y1 == kä and y2 == sa:
        print("Tervetuloa")
        break
    else:
        print("Pääsy evätty")
        y = y + 1