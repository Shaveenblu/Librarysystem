from magazinemodel import Magazine


def print_info(magazine):
    print(f"Magazine NO: {magazine.magazine_no},Title: {magazine.title}, Color: {magazine.color},Subject: {magazine.subject}, Rental Price per day: {magazine.rental_price}, Number of Copies:{magazine.no_copies}")


class MagazineFunction:
    def __init__(self):
        self.list_of_magazine = []
        self.__initial_data()

    def __initial_data(self):
        a_magazine1 = Magazine(magazine_no="01",title="History of Cricket", color="color", subject="Science", rental_price=5.00, no_copies=7)
        a_magazine2 = Magazine(magazine_no="02",title="Evolution of the Computer", color="black&white", subject="Technology", rental_price=3.00, no_copies=21)
        self.list_of_magazine.append(a_magazine1)
        self.list_of_magazine.append(a_magazine2)

    def add(self):
        __magazine = input("Enter magazine number: ")
        __title = input("Enter title of the magazine: ")
        __color = input("Color Black or black & white: ")
        __subject = input("Enter Subject")
        __rental_price = input("Enter rental price per day: ")
        __no_copies = input("Enter number of copies: ")

        magazine = Magazine(magazine_no=__magazine,title=__title, color=__color, subject=__subject,rental_price=__rental_price, no_copies=__no_copies)
        self.list_of_magazine.append(magazine)
        print(f"{magazine.color} Magazine added  with magazine no. {magazine.magazine_no}")

    print()

    def remove(self):
        __magazine = input("Enter magazine number: ")
        __color = input("Color Black or black & white: ")
        __subject = input("Enter Subject: ")
        __rental_price = input("Enter rental price per day: ")
        __no_copies = input("Enter number of copies: ")

        matched_data = list(x for x in self.list_of_magazine if x.magazine_no == __magazine)
        for x in matched_data:
            self.list_of_magazine.remove(x)
            print("Item Removed.")

    def lend(self):
        __magazine = input("Enter magazine number: ")
        __title = input("Enter title of the magazine: ")
        __color = input("Color Black or black & white: ")
        __subject = input("Enter Subject: ")
        __rental_price = input("Enter rental price per day: ")
        __no_copies = int(input("Enter number of copies: "))

        matched_data = list(x for x in self.list_of_magazine if x.magazine_no == __magazine)
        for x in matched_data:
            x.no_copies -= __no_copies
            print("Magazine Lent")

    def receive(self):
        __magazine = input("Enter magazine number: ")
        __title = input("Enter title of the magazine: ")
        __color = input("Color Black or black & white: ")
        __subject = input("Enter Subject: ")
        __rental_price = input("Enter rental price per day: ")
        __no_copies = int(input("Enter number of copies: "))

        matched_data = list(x for x in self.list_of_magazine if x.magazine_no == __magazine)
        for x in matched_data:
            x.no_copies += __no_copies
            print("Magazine received with Copies")

    def display_all(self):
        for x in self.list_of_magazine:
            print_info(magazine=x)

    def display_available(self):
        matched_data = list(x for x in self.list_of_magazine if x.no_copies > 0)
        for x in matched_data:
            print_info(magazine=x)

    def display_unavailable(self):
        matched_data = list(x for x in self.list_of_magazine if x.no_copies == 0)
        for x in matched_data:
            print_info(magazine=x)
