# models.py
from db_config import DB_CONFIG
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# Get all artworks
def get_all_artworks():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT a.artwork_id, a.title, a.year, a.type, a.price, a.rating, ar.name AS artist
        FROM Artwork a
        LEFT JOIN Artist ar ON a.artist_id = ar.artist_id
    """)
    results = cursor.fetchall()
    db.close()
    return results

# Add artwork (create artist if doesn't exist)
def add_artwork(title, artist_name, year, art_type, price, rating=None):
    db = get_db_connection()
    cursor = db.cursor()

    # Find artist_id
    cursor.execute("SELECT artist_id FROM Artist WHERE name = %s", (artist_name,))
    artist = cursor.fetchone()

    if artist:
        artist_id = artist[0]
    else:
        cursor.execute("INSERT INTO Artist (name) VALUES (%s)", (artist_name,))
        db.commit()
        artist_id = cursor.lastrowid

    # Insert artwork
    cursor.execute(
        "INSERT INTO Artwork (title, year, type, price, rating, artist_id) VALUES (%s, %s, %s, %s, %s, %s)",
        (title, year, art_type, price, rating, artist_id)
    )
    db.commit()
    db.close()

# Get artworks of a specific artist
def get_artworks_by_artist(artist_name):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT a.artwork_id, a.title, a.year, a.type, a.price, a.rating
        FROM Artwork a
        JOIN Artist ar ON a.artist_id = ar.artist_id
        WHERE ar.name = %s
    """, (artist_name,))
    results = cursor.fetchall()
    db.close()
    return results

# Delete artwork
def delete_artwork(artwork_id):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM Artwork WHERE artwork_id = %s", (artwork_id,))
    db.commit()
    db.close()

# Update artwork rating
def update_artwork_rating(artwork_id, rating):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("UPDATE Artwork SET rating = %s WHERE artwork_id = %s", (rating, artwork_id))
    db.commit()
    db.close()
