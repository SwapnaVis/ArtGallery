import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Artdbms@25",  # <-- change this
    database="art_gallery"
)

cursor = db.cursor()

def list_artists():
    cursor.execute("SELECT * FROM Artist")
    for artist in cursor.fetchall():
        print(artist)

list_artists()

cursor.close()
db.close()
