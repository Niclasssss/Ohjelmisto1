def hae_kentta():
    sql = f"SELECT name, municipality FROM airport WHERE ident =%s"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql, (lentokenttä,))
    tulos = kursori.fetchone()
    if tulos:
        nimi = tulos[0]
        kaupunki = tulos[1]
        print(f"Airport name: {nimi}\nLocation: {kaupunki}")
    else:
        print(f"No airport found with ICAO code {lentokenttä}")
    return

import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='pythonukko1',
         password='89tyo22.maa64434dii',
         autocommit=True
         )

lentokenttä = input("Enter the ICAO code of an airport: ").upper()
hae_kentta()