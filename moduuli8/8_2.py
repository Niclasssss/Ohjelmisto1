def get_airports_by_country(country_code):
    sql = f"SELECT type, count(*) FROM airport WHERE iso_country =%s GROUP BY type"
    kursori = yhteys.cursor()
    kursori.execute(sql, (country_code,))
    tulos = kursori.fetchall()
    return tulos

def run_country_program():
    syöte = input("Enter the country code (e.g., FI for Finland): ").upper()
    tulos = get_airports_by_country(syöte)
    if tulos:
        print(f"Airports in {syöte}: ")
        for rivi in tulos:
            print(f"{rivi[1]} {rivi[0]} airports")
    else:
        print(f"No airports found for country code '{syöte}'.")

import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='pythonukko1',
         password='89tyo22.maa64434dii',
         autocommit=True
         )

run_country_program()