# ui.py



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
       

        # Call the appropriate function from library_manager to add the book
        self.library_manager.add_book(isbn, title)
        print("Book added successfully!")

    def borrow_book(self):
        isbn = input("Enter the ISBN of the book you want to borrow: ")
        person_id = input("Enter your person ID: ")

        # Call the appropriate function from library_manager to borrow the book
        is_borrowed = self.library_manager.assign_book_to_user(isbn, person_id)
        if is_borrowed:
            print("Book borrowed successfully!")
        else:
            print("Book not available for borrowing or user not registered.")
