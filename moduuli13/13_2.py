from flask import Flask, jsonify
import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='pythonukko1',
    password='89tyo22.maa64434dii',
    autocommit=True
)

def airport(icao):
    sql = f"select ident, name, municipality from airport where ident='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    return tulos

app = Flask(__name__)
@app.route('/kenttä/<icao>')
def palauta(icao):
    tulos = airport(icao)
    vastaus = {
        "ICAO": tulos[0],
        "name": tulos[1],
        "Municipality": tulos[2]
    }
    return jsonify(vastaus)

app.run(use_reloader=True, host='127.0.0.1', port=3000)