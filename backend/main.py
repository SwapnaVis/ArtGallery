from controllers import show_all_artworks, create_artwork, show_artist_artworks, remove_artwork, rate_artwork

def menu():
    while True:
        print("\n--- Art Gallery Menu ---")
        print("1. Show all artworks")
        print("2. Add new artwork")
        print("3. Show artworks by specific artist")
        print("4. Delete artwork")
        print("5. Rate an artwork")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_all_artworks()
        elif choice == "2":
            create_artwork()
        elif choice == "3":
            show_artist_artworks()
        elif choice == "4":
            remove_artwork()
        elif choice == "5":
            rate_artwork()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
