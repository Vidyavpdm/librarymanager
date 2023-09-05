

from library_manager.book import Book

class UserInterface:
    def __init__(self, library_manager):
        self.library_manager = library_manager

    def show_menu(self):
        while True:
            print("\n===== Library Manager Menu =====")
            print("1. Add Book")
            print("2. Borrow Book")
            print("3. Exit")

            choice = input("Enter your choice (1/2/3): ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.borrow_book()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_book(self):
        isbn = input("Enter the ISBN of the book: ")
        title = input("Enter the title of the book: ")
   
        book = Book(title, isbn)

    # Call the appropriate function from library_manager to add the book
        self.library_manager.add_book(book)
        print("Book added successfully!")

    def borrow_book(self):
            person_id = input("Enter your person ID: ")

    # Debug: Print registered users
            print("Registered Users:", self.library_manager.registered_users)

    # Check if the user is registered
            if not self.library_manager.is_user_registered(person_id):
                print(f"User with ID '{person_id}' is not registered. Please register first.")
                return

            isbn = input("Enter the ISBN of the book you want to borrow: ")

    # Call the appropriate function from library_manager to borrow the book
            is_borrowed = self.library_manager.assign_book_to_user(isbn, person_id)
            if is_borrowed:
                 print(f"Book with ISBN '{isbn}' has been assigned to person with ID '{person_id}'.")
            else:
                 print("Book not available for borrowing or user not registered.")

  