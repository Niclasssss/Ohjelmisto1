#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C)
#ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
#Tehtävässä on käytettävä if/elif/else-toistorakennetta.
#LUX on parvekkeellinen hytti yläkannella.
#A on ikkunallinen hytti autokannen yläpuolella.
#B on ikkunaton hytti autokannen yläpuolella.
#C on ikkunaton hytti autokannen alapuolella.
#Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

hl = input("Anna laivan hyttiluokka: ")
if hl == "LUX":
    print("LUX on parvekkeellinen hytti autokannen yläpuolella")
elif hl == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella")
elif hl == "B":
    print("B on ikkunaton hytti autokannan puolella")
elif hl == "C":
    print("C on ikkunaton hytti autokannan alapuolella")
else:
    print("Virheellinen hyttiluokka")