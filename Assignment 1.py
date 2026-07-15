from datetime import datetime

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            return False
        self.is_borrowed = True
        return True

    def return_book(self):
        if not self.is_borrowed:
            return False
        self.is_borrowed = False
        return True

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = {}

    def borrow_book(self, book: Book):
        if book.borrow():
            self.borrowed_books[book.book_id] = datetime.now().strftime("%Y-%m-%d")
            return True
        return False

    def return_book(self, book: Book):
        if book.book_id in self.borrowed_books and book.return_book():
            del self.borrowed_books[book.book_id]
            return True
        return False

    def __str__(self):
        return f"Patron {self.patron_id}: {self.name} | Borrowed: {list(self.borrowed_books.keys())}"


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print(f"Book ID {book_id} already exists.")
            return
        self.books[book_id] = Book(book_id, title, author)
        print(f"Book '{title}' added successfully.")

    def register_patron(self, patron_id, name):
        if patron_id in self.patrons:
            print(f"Patron ID {patron_id} already exists.")
            return
        self.patrons[patron_id] = Patron(patron_id, name)
        print(f"Patron '{name}' registered successfully.")

    def borrow_book(self, patron_id, book_id):
        patron = self.patrons.get(patron_id)
        book = self.books.get(book_id)

        if not patron:
            print("Patron not found.")
            return
        if not book:
            print("Book not found.")
            return

        if patron.borrow_book(book):
            print(f"Book '{book.title}' borrowed by {patron.name}.")
        else:
            print(f"Book '{book.title}' is already borrowed.")

    def return_book(self, patron_id, book_id):
        patron = self.patrons.get(patron_id)
        book = self.books.get(book_id)

        if not patron:
            print("Patron not found.")
            return
        if not book:
            print("Book not found.")
            return

        if patron.return_book(book):
            print(f"Book '{book.title}' returned by {patron.name}.")
        else:
            print(f"{patron.name} did not borrow '{book.title}'.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books.values():
            print(book)

    def display_patrons(self):
        if not self.patrons:
            print("No patrons registered.")
            return
        for patron in self.patrons.values():
            print(patron)


def main():
    library = Library()

    while True:
        print("\n Library Menu:")
        print("1. Add Book")
        print("2. Register Patron")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Display Patrons")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            library.add_book(book_id, title, author)

        elif choice == "2":
            patron_id = int(input("Enter Patron ID: "))
            name = input("Enter Patron Name: ")
            library.register_patron(patron_id, name)

        elif choice == "3":
            patron_id = int(input("Enter Patron ID: "))
            book_id = int(input("Enter Book ID: "))
            library.borrow_book(patron_id, book_id)

        elif choice == "4":
            patron_id = int(input("Enter Patron ID: "))
            book_id = int(input("Enter Book ID: "))
            library.return_book(patron_id, book_id)

        elif choice == "5":
            print("\n List of Books:")
            library.display_books()

        elif choice == "6":
            print("\n List of Patrons:")
            library.display_patrons()

        elif choice == "7":
            print("Exiting Library System. Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
##Library Menu:
##1. Add Book
##2. Register Patron
##3. Borrow Book
##4. Return Book
##5. Display Books
##6. Display Patrons
##7. Exit
##Enter your choice: 1
##Enter Book ID: 101
##Enter Book Title: Python sem 2 text
##Enter Author Name: Joy Chikhaliya
##Book 'Python sem 2 text' added successfully.
##
## Library Menu:
##1. Add Book
##2. Register Patron
##3. Borrow Book
##4. Return Book
##5. Display Books
##6. Display Patrons
##7. Exit
##Enter your choice: 2
##Enter Patron ID: 1001
##Enter Patron Name: Joy Chikhaliya
##Patron 'Joy Chikhaliya' registered successfully.
##
## Library Menu:
##1. Add Book
##2. Register Patron
##3. Borrow Book
##4. Return Book
##5. Display Books
##6. Display Patrons
##7. Exit
##Enter your choice: 3
##Enter Patron ID: 1001
##Enter Book ID: 101
##Book 'Python sem 2 text' borrowed by Joy Chikhaliya.
##
## Library Menu:
##1. Add Book
##2. Register Patron
##3. Borrow Book
##4. Return Book
##5. Display Books
##6. Display Patrons
##7. Exit
##Enter your choice: 4
##Enter Patron ID: 1001
##Enter Book ID: 101
##Book 'Python sem 2 text' returned by Joy Chikhaliya.
##
## Library Menu:
##1. Add Book
##2. Register Patron
##3. Borrow Book
##4. Return Book
##5. Display Books
##6. Display Patrons
##7. Exit
##Enter your choice: 5
##
## List of Books:
##[101] Python sem 2 text by Joy Chikhaliya - Available
##
## Library Menu:
##1. Add Book
##2. Register Patron
##3. Borrow Book
##4. Return Book
##5. Display Books
##6. Display Patrons
##7. Exit
##Enter your choice: 6
##
## List of Patrons:
##Patron 1001: Joy Chikhaliya | Borrowed: []
##
## Library Menu:
##1. Add Book
##2. Register Patron
##3. Borrow Book
##4. Return Book
##5. Display Books
##6. Display Patrons
##7. Exit
##Enter your choice:
