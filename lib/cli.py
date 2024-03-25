from db.database import Database

class CLI:
    def __init__(self):
        self.db = Database("books.db")

    def display_menu(self):
        print("Welcome to the E-book Manager")
        print("1. Add an Author")
        print("2. Add a Book")
        print("3. Display Authors")
        print("4. Display Books")
        print("5. Delete Book")
        print("6. Get Books by Author")
        print("7. Get Books by Year of Publish")
        print("8. Get Books by Category")
        print("9. Exit")

    def create_author(self):
        name = input("Enter the author's name: ")
        author = self.db.create_author(name)
        if author:
            print(f"Author {author.name} created successfully.")
        else:
            print(f"Failed to create author")


    def create_book(self):
        title = input("Enter the book's title: ")
        category= input("Enter the category of the book: ")
        year_of_publish= input("Enter the year of publish: ")
        copies_sold= input("Enter the number of copies sold: ")
        author_name = input("Enter the author's name: ")

        book = self.db.create_book(title, category, year_of_publish, copies_sold, author_name)
        if book:
            print(f"Book '{book.title}' by '{author_name}' created successfully.")
        else:
            print(f"Failed to create book '{title}'.")

    def display_authors(self):
        print("Authors:")
        authors = self.db.get_all_authors()
        for author in authors:
            print(author)

    def display_books(self):
        print("Books:")
        books = self.db.get_all_books()
        for book in books:
            author = self.db.find_author_by_id(book.author_id)
            print(f"Title: {book.title}")
            print(f"Category: {book.category}")
            print(f"Year of Publish: {book.year_of_publish}")
            print(f"Copies Sold: {book.copies_sold}")
            print(f"Author: {author.name}")
            print()
            
    def delete_book(self):
        book_id = input("Enter the ID of the book you want to delete: ")
        success = self.db.delete_book(book_id)
        if success:
            print("Book deleted successfully.")
        else:
            print("Failed to delete book. Please check the ID.")

    def get_books_by_author(self):
        author_name = input("Enter the author's name: ")
        books = self.db.get_books_by_author(author_name)
        if books:
            print(f"Books by {author_name}:")
            for book in books:
                print(book)
        else:
            print(f"No books found by {author_name}.")

    def get_books_by_year(self):
        year = input("Enter the year of publish: ")
        books = self.db.get_books_by_year(year)
        if books:
            print(f"Books published in {year}:")
            for book in books:
                print(book)
        else:
            print(f"No books found published in {year}.")

    def get_books_by_category(self):
        category = input("Enter the category of books: ")
        books = self.db.get_books_by_category(category)
        if books:
            print(f"Books in category '{category}':")
            for book in books:
                print(book)
        else:
            print(f"No books found in category '{category}'.")

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
                self.delete_book()
            elif choice == "6":
                self.get_books_by_author()
            elif choice == "7":
                self.get_books_by_year()
            elif choice == "8":
                self.get_books_by_category()
            elif choice == "9":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    cli = CLI()
    cli.run()
