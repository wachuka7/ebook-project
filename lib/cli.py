import sys
from db.database import Database

class CLI:
    def __init__(self):
        self.db = Database("books.db")

    def display_menu(self):
        print("Welcome to the E-book Manager")
        print("1. Create Author")
        print("2. Create Book")
        print("3. Display Authors")
        print("4. Display Books")
        print("5. Exit")

    def create_author(self):
        name = input("Enter the author's name: ")
        author = self.db.create_author(name)
        print(f"Author {author.name} created successfully.")

    def create_book(self):
        title = input("Enter the book's title: ")
        author_name = input("Enter the author's name: ")
        author = self.db.find_author_by_name(author_name)
        if author:
            book = self.db.create_book(title, author)
            print(f"Book {book.title} by {book.author.name} created successfully.")
        else:
            print(f"Author {author_name} does not exist.")

    def display_authors(self):
        print("Authors:")
        for author in self.db.authors:
            print(author)

    def display_books(self):
        print("Books:")
        for book in self.db.books:
            print(book)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_author()
            elif choice == "2":
                self.create_book()
            elif choice == "3":
                self.display_authors()
            elif choice == "4":
                self.display_books()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    cli = CLI()
    cli.run()
