kaupungit = []

for i in range(5):
  kaupunki = input("Enter the name of a city: ")
  kaupungit.append(kaupunki)

print("The cities you entered: ")
for kaupunki in kaupungit:
  print(kaupunki)