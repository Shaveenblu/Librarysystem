from bookmodel import Book

def print_info(book):
    print(f"ISBN NO: {book.isbn_no}, Title: {book.title}, Format: {book.book_format}, Subject: {book.subject}, Rental Price per day: {book.rental_price}, Number of Copies:{book.no_copies}")

#if function inside the class one arguemnt is compulsory self=reference(instance) same class
class BookFunction:
    def __init__(self):
        self.list_of_books = []
        #private init encapusalution
        self.__initial_data()

    def __initial_data(self):
        a_book1 = Book(isbn_no="ISBN01234", title="The Solar System", book_format="Hardcover", subject="Science", rental_price=15.50, no_copies=5)
        a_book2 = Book(isbn_no="ISBN9876", title="Types of Animal Species", book_format="Paperback", subject="Science", rental_price= 10.00, no_copies=8)
        a_book3 = Book(isbn_no="ISBN1290", title="Second World War", book_format="Hardcover", subject="History",rental_price=12.50, no_copies=0)
        self.list_of_books.append(a_book1)
        self.list_of_books.append(a_book2)
        self.list_of_books.append(a_book3)

    def add(self):
        __isbn = input("Enter ISBN Number: ")
        __title = input("Enter title: ")
        __book_format = input("Enter book format: ")
        __subject = input("Enter subject: ")
        __rental_price = input("Enter price per day: ")
        __copies = input("Enter copies: ")

        book = Book(isbn_no=__isbn, title=__title, book_format=__book_format, subject=__subject, rental_price=__rental_price, no_copies=__copies)
        self.list_of_books.append(book)
        print(f"{book.title} Book added  with ISBN {book.isbn_no}")


    def remove(self):
        __isbn = input("Enter ISBN Number: ")
        __title = input("Enter title: ")
        __book_format = input("Enter book format: ")
        __subject = input("Enter subject: ")
        __rental_price = input("Enter price per day: ")
        __copies = input("Enter copies: ")

        matched_data = list(x for x in self.list_of_books if x.isbn_no==__isbn)
        for x in matched_data:
            self.list_of_books.remove(x)
            print("Item Removed.")
    
    def lend(self):
        __isbn = input("Enter ISBN Number: ")
        __title = input("Enter title: ")
        __book_format = input("Enter book format: ")
        __subject = input("Enter subject: ")
        __rental_price = input("Enter price per day: ")
        __copies = int(input("Enter copies: "))

        matched_data = list(x for x in self.list_of_books if x.isbn_no == __isbn)
        for x in matched_data:
            x.no_copies -= __copies
            print("Book Lent")

    def receive(self):
        __isbn = input("Enter ISBN number:")
        __title = input("Enter title: ")
        __book_format = input("Enter book format: ")
        __subject = input("Enter subject: ")
        __rental_price = input("Enter price per day: ")
        __copies = int(input("Enter received copies count: "))

        matched_data = list(x for x in self.list_of_books if x.isbn_no == __isbn)
        for x in matched_data:
            x.no_copies += __copies
            print("Received copies of the book")

    def display_all(self):
        for x in self.list_of_books:
            print_info(book=x)

    def display_available(self):
        matched_data = list(x for x in self.list_of_books if x.no_copies > 0)
        for x in matched_data:
            print_info(book=x)

    def display_unavailable(self):
        matched_data = list(x for x in self.list_of_books if x.no_copies == 0)
        for x in matched_data:
            print_info(book=x)






        

