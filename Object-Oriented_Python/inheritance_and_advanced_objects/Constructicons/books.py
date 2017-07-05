class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '{} by {}'.format(self.title, self.author)

class Bookcase:

    def __init__(self, books = None): # takes list of books
        self.books = books

    @classmethod
    def create_bookcase(cls, book_list):
        books = []
        for title, author in book_list:
            books.append(Book(title, author))
        return cls(books) # return instance of the class with list of books
        # books created here gets passed to init

