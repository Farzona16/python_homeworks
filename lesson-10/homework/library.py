class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def __str__(self):
        return f"{self.title} by {self.author} ({'Borrowed' if self.is_borrowed else 'Available'})"

class Member:
    books_limit = 3
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.books_limit:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than {self.books_limit} books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"The book '{book.title}' is already borrowed.")
        book.is_borrowed = True
        self.borrowed_books.append(book)
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
        
    def __str__(self):
        borrowed_titles = ', '.join([book.title for book in self.borrowed_books]) or "No books borrowed"
        return f"Member: {self.name}, Borrowed Books: {borrowed_titles}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
    
    def add_book(self, title, author):
        if title in self.books:
            print(f"The book '{title}' already exists in the library.")
            return
        book = Book(title, author)
        self.books[title] = book
    
    def add_member(self, name):
        if name in self.members:
            print(f"Member '{name}' already exists.")
            return
        member = Member(name)
        self.members[name] = member
    
    def borrow_book(self, member_name, book_title):
        if book_title not in self.books:
            raise BookNotFoundException(f"The book '{book_title}' is not available in the library.")
        if member_name not in self.members:
            print(f"Member '{member_name}' not found. Please register first.")
            return
        member = self.members[member_name]
        book = self.books[book_title]
        try:
            member.borrow_book(book)
            print(f"'{book_title}' has been borrowed by {member_name}.")
        except (BookAlreadyBorrowedException, MemberLimitExceededException) as e:
            print(e)
    
    def return_book(self, member_name, book_title):
        if member_name in self.members and book_title in self.books:
            member = self.members[member_name]
            book = self.books[book_title]
            member.return_book(book)
            print(f"'{book_title}' has been returned by {member_name}.")
    
    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        for book in self.books.values():
            print(book)
    
    def display_members(self):
        if not self.members:
            print("No members registered in the library.")
            return
        for member in self.members.values():
            print(member)

if __name__ == "__main__":
    library = Library()
    library.add_book("First book", "1 Author")
    library.add_book("2nd book", "2 Author")
    library.add_book("Book3", "Author3")
    
    library.add_member("Alice")
    library.add_member("Bob")
    try:
        library.borrow_book("Alice", "First book")
        library.borrow_book("Alice", "2nd book")
        library.borrow_book("Alice", "Book3")
        library.borrow_book("Alice", "B")  
    except Exception as e:
        print(f"Error: {e}")         

    print("\nBooks in Library:")
    library.display_books()
    print("\nLibrary Members:")
    library.display_members()
    
    
    library.return_book("Alice", "2nd book")
    print("\nAfter returning '2nd book':")
    library.display_members()
