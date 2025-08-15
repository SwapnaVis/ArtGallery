from models import get_all_artworks, add_artwork, get_artworks_by_artist, delete_artwork, update_artwork_rating

# Show all artworks
def show_all_artworks():
    artworks = get_all_artworks()
    if not artworks:
        print("No artworks found.")
        return
    for art in artworks:
        print(f"{art['artwork_id']}. {art['title']} ({art['year']}), {art['type']} - ${art['price']} | Rating: {art['rating']} | Artist: {art['artist']}")

# Add new artwork
def create_artwork():
    title = input("Enter title: ")
    artist = input("Enter artist: ")
    year = int(input("Enter year: "))
    art_type = input("Enter type (Painting, Sculpture, etc.): ")
    price = float(input("Enter price: "))
    rating = float(input("Enter rating (0.0 - 5.0): "))
    add_artwork(title, artist, year, art_type, price, rating)
    print("Artwork added successfully!")

# Show artworks of specific artist
def show_artist_artworks():
    artist_name = input("Enter artist name: ")
    artworks = get_artworks_by_artist(artist_name)
    if not artworks:
        print("No artworks found for this artist.")
        return
    for art in artworks:
        print(f"{art['artwork_id']}. {art['title']} ({art['year']}), {art['type']} - ${art['price']} | Rating: {art['rating']}")

# Delete artwork
def remove_artwork():
    artwork_id = int(input("Enter Artwork ID to delete: "))
    delete_artwork(artwork_id)
    print("Artwork deleted successfully!")

# Update artwork rating
def rate_artwork():
    artwork_id = int(input("Enter Artwork ID to rate: "))
    rating = float(input("Enter new rating (0.0 - 5.0): "))
    update_artwork_rating(artwork_id, rating)
    print("Rating updated successfully!")
