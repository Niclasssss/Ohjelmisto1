#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
#Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.

luoti = 13.3
naula = 32*(luoti)
leiviskä = 20*(naula)

luodit = float(input("Anna luodit: "))
naulat = float(input("Anna naulat: "))
leiviskät = float(input("Anna leiviskät: "))

v1 = luoti * luodit
v2 = naula * naulat
v3 = leiviskä * leiviskät

koko = v1 + v2 + v3
print(koko/1000, "kg")