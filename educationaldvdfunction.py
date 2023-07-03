from educationaldvdmodel import DVD


def print_info(dvd):
    print(f"DVD NO: {dvd.dvd_no}, Title: {dvd.title},Subject: {dvd.subject}, Rental Price per day: {dvd.rental_price}, Number of Copies:{dvd.no_copies}")


class DVDFunction:
    def __init__(self):
        self.list_of_dvd = []
        self.__initial_data()

    def __initial_data(self):
        a_dvd1 = DVD(dvd_no="10", title=" Birth of the Solar System,",subject="Astronomy", rental_price=2.50, no_copies=10)
        a_dvd2 = DVD(dvd_no="11", title="Pythagoras Theorem",subject="Math", rental_price=1.00, no_copies=50)
        self.list_of_dvd.append(a_dvd1)
        self.list_of_dvd.append(a_dvd2)

    def add(self):
        __dvd = input("Enter DVD number: ")
        __title = input("Enter title: ")
        __subject = input("Enter subject: ")
        __rental_price = input("Enter rental pricer per day: ")
        __copies = input("Enter number of copies: ")

        dvd = DVD(dvd_no=__dvd, title=__title,subject=__subject,rental_price=__rental_price, no_copies=__copies)
        self.list_of_dvd.append(dvd)
        print(f"{dvd.title} DVD added  with DVD no. 3{dvd.dvd_no}")

    print()

    def remove(self):
        __dvd = input("Enter DVD number: ")
        __title = input("Enter title: ")
        __subject = input("Enter subject: ")
        __rental_price = input("Enter rental pricer per day: ")
        __copies = input("Enter number of copies: ")

        matched_data = list(x for x in self.list_of_dvd if x.dvd_no == __dvd)
        for x in matched_data:
            self.list_of_dvd.remove(x)
            print("Item Removed.")

    def lend(self):
        __dvd = input("Enter DVD number: ")
        __title = input("Enter title: ")
        __subject = input("Enter subject: ")
        __rental_price = input("Enter rental pricer per day: ")
        __copies = int(input("Enter number of copies: "))

        matched_data = list(x for x in self.list_of_dvd if x.dvd_no == __dvd)
        for x in matched_data:
            x.no_copies -= __copies
            print("DVD Lent")

    def receive(self):
        __dvd = input("Enter DVD number; ")
        __title = input("Enter title: ")
        __subject = input("Enter subject: ")
        __rental_price = input("Enter rental pricer per day: ")
        __copies = int(input("Enter number of copies: "))

        matched_data = list(x for x in self.list_of_dvd if x.dvd_no == __dvd)
        for x in matched_data:
            x.no_copies += __copies
            print("DVD received")

    def display_all(self):
        for x in self.list_of_dvd:
            print_info(dvd=x)

    def display_available(self):
        matched_data = list(x for x in self.list_of_dvd if x.no_copies > 0)
        for x in matched_data:
            print_info(dvd=x)

    def display_unavailable(self):
        matched_data = list(x for x in self.list_of_dvd if x.no_copies == 0)
        for x in matched_data:
            print_info(dvd=x)



