class LibrarySystem:
    def __init__(self):
        self.books = {
            "101": {"title": "Introduction to Python", "author": "John Smith", "available": True},
            "102": {"title": "Data Science Handbook", "author": "Emily Johnson", "available": True},
            "103": {"title": "Artificial Intelligence Basics", "author": "David Miller", "available": True}
        }
        self.users = {}
        self.borrowed_books = {}

    def borrow_book(self, user_id, book_id):
        if book_id in self.books and self.books[book_id]["available"]:
            self.books[book_id]["available"] = False
            self.borrowed_books.setdefault(user_id, []).append(book_id)
            print(f"Book '{self.books[book_id]['title']}' borrowed successfully by user {user_id}.")
        else:
            print("Book not available for borrowing.")

    def return_book(self, user_id, book_id):
        if user_id in self.borrowed_books and book_id in self.borrowed_books[user_id]:
            self.books[book_id]["available"] = True
            self.borrowed_books[user_id].remove(book_id)
            print(f"Book '{self.books[book_id]['title']}' returned successfully by user {user_id}.")
        else:
            print("Book not borrowed by this user.")

    def display_books(self):
        print("Available Books:")
        for book_id, book_info in self.books.items():
            if book_info["available"]:
                print(f"{book_id}: {book_info['title']} by {book_info['author']}")

    def run_system(self):
        print("Welcome to the Library System!")
        while True:
            print("\n1. Display Available Books")
            print("2. Borrow a Book")
            print("3. Return a Book")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.display_books()
            elif choice == "2":
                user_id = input("Enter your user ID: ")
                book_id = input("Enter the book ID you want to borrow: ")
                self.borrow_book(user_id, book_id)
            elif choice == "3":
                user_id = input("Enter your user ID: ")
                book_id = input("Enter the book ID you want to return: ")
                self.return_book(user_id, book_id)
            elif choice == "4":
                print("Thank you for using the Library System!")
                break
            else:
                print("Invalid choice. Please try again.")

# Instantiate and run the library system
library = LibrarySystem()
library.run_system()
