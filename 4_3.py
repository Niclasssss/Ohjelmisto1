#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
#kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

Luvut = []

luku = input("Anna luku: ")
while luku!="":
    Luvut.append(float(luku))
    luku = input("Anna seuraava luku tai lopeta painamalla enter: ")
print(f"Pienin luku on: {min(Luvut)}")
print(f"Suurin luku on: {max(Luvut)}")