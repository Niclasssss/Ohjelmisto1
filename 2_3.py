#Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
#Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
#Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

k = input("Anna suorakulmion kanta: ")
ka = float(k)
p = input("Anna suorakulmion korkeus: ")
ko = float(p)

pi = 2 * (ka + ko)
pa = ka * ko

print("Piiri on", pi)
print("Pinta-Ala on",  pa)