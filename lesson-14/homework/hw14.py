import requests
import json
import random
# 1. write a Python script that reads the students.jon JSON file and prints details of each student.
filename = "students.json"
with open (filename, 'r') as file:
    data = json.load(file)
    print(data)
# 2. Use this url : https://openweathermap.org/
# Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).
CITY = 'Tashkent'
API_KEY = '29dd35ffcb98ba41efd4fb24b525157c'
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
r = requests.get(URL)

if r.status_code == 200:
    data = r.json()
    print(f'City: {CITY}')
    print(f'Weather: {data["weather"][0]['main']}' )
    print(f'Temperature: {data["main"]["temp"]}')
    print(f'Humidity: {data["main"]["humidity"]}')
else:
    print('Failed to get weather information')


# 3. Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.
BOOKS_FILE = "books.json"

def load_books():
    with open(BOOKS_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            print(f"{BOOKS_FILE} file is not found.")

def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")
    books = load_books()
    books.append({"title": title, "author": author, "year": year})
    save_books(books)
    print(f"Book '{title}' added successfully!")

def update_book():
    books = load_books()
    title = input("Enter the title of the book to update: ")

    for book in books:
        if book["title"].lower() == title.lower():
            print("Enter new details (leave blank to keep existing values):")
            new_author = input(f"New author [{book['author']}]: ") or book["author"]
            new_year = input(f"New year [{book['year']}]: ") or book["year"]

            book["author"], book["year"], book["isbn"] = new_author, new_year
            save_books(books)
            print(f"Book '{title}' updated successfully!")
            return

    print("Book not found.")

def delete_book():
    books = load_books()
    title = input("Enter the title of the book to delete: ")

    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            save_books(books)
            print(f"Book '{title}' deleted successfully!")
            return

    print("Book not found.")


def main():
    while True:
        print("\nBook Manager")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

main()
# 4. Use this url http://www.omdbapi.com/ to fetch information about movies.
# Create a program that asks users for a movie genre and recommends a random movie from that genre.
API_KEY = "8fe32e29"
BASE_URL = "http://www.omdbapi.com/"
# https://www.omdbapi.com/?i=tt3896198&apikey=8fe32e29
def get_movies_by_genre(genre):
    search_url = f"{BASE_URL}?apikey={API_KEY}&s={genre}&type=movie"
    response = requests.get(search_url)

    if response.status_code != 200:
        print("Error fetching data!")
        return None

    data = response.json()

    if "Search" not in data:
        print("No movies found for this genre!")
        return None

    return data["Search"]

def recommend_movie():
    genre = input("Enter a movie genre (e.g., Action, Comedy, Drama): ")
    movies = get_movies_by_genre(genre)

    if movies:
        movie = random.choice(movies)
        print("Recommended Movie:")
        print(f"Title: {movie['Title']}")
        print(f"Year: {movie['Year']}")
        print(f"IMDB ID: {movie['imdbID']}")
    else:
        print("Try a different genre.")

recommend_movie()