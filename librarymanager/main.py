# main.py
# main.py

from library_manager.ui import UserInterface
from library_manager.librarymanger import LibraryManager

def main():
    # Initialize the LibraryManager instance
    library_manager = LibraryManager()

    # Create the UserInterface instance and pass the library_manager to it
    ui = UserInterface(library_manager)

    # Show the interactive menu
    ui.show_menu()

if __name__ == "__main__":
    main()

LibraryManager