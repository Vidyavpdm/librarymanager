class Book:
    def __init__(self, name, ISBN):
        self.name=name
        self.ISBN = ISBN

    def __str__(self):
        return f"Book<{self.name}>"
book = Book("DO 1234 EPIC SHIT", "78463738")

print(book)

