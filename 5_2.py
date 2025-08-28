#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
#Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

luvut = []

luku = int(input("Anna luku tai lopeta painamalla enter: "))
while luku!="":
    luvut.append(int(luku))
    luku = input("Anna luku tai lopeta painamalla enter: ")
luvut.sort(reverse=True)

for i in luvut[:5]:
    print(i)