
from library_manager.ui import UserInterface
from library_manager.librarymanger import LibraryManager
from library_manager.book import Book

def main():
 
    library_manager = LibraryManager()


    ui = UserInterface(library_manager)

  
    ui.show_menu()

if __name__ == "__main__":
    main()



