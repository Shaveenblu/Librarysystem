from LectureCDmodel import LectureCD


def print_info(lec_cd):
    print(f"Lecture Cd No: {lec_cd.cd_no}, Title: {lec_cd.title}, Subject: {lec_cd.subject}, Rental Price: {lec_cd.rental_price}, Available Copies:{lec_cd.copies}")


class LectureCDFunction:
    def __init__(self):
        self.list_of_lec_cd = []
        self.__initial_data()

    def __initial_data(self):
        a_lec_cd1 = LectureCD(cd_no="21", title="Basics of Western Music",subject="Music", rental_price=1.50, copies=11)
        a_lec_cd2 = LectureCD(cd_no="22", title="Japanese Language",subject="Foreign Languages", rental_price=2.00, copies=3)
        self.list_of_lec_cd.append(a_lec_cd1)
        self.list_of_lec_cd.append(a_lec_cd2)

    def add(self):
        __cd = input("Enter CD number: ")
        __title = input("Enter title: ")
        __subject = input("Enter subject: ")
        __rental_price = input("Enter rental price per day: ")
        __copies = input("Enter number of copies: ")

        lec_cd = LectureCD(cd_no=__cd, title=__title,subject=__subject,rental_price=__rental_price, copies=__copies)
        self.list_of_lec_cd.append(lec_cd)
        print(f"{lec_cd.title} Lecture CD added  with cd no. {lec_cd.cd_no}")

    print()

    def remove(self):
        __cd = input("Enter CD number: ")
        __title = input("Enter title: ")
        __subject = input("Enter subject: ")
        __rental_price = input("Enter rental price per day: ")
        __copies = input("Enter number of copies: ")

        matched_data = list(x for x in self.list_of_lec_cd if x.cd_no == __cd)
        for x in matched_data:
            self.list_of_lec_cd.remove(x)
            print("Item Removed.")

    def lend(self):
        __cd = input("Enter CD number: ")
        __title = input("Enter title: ")
        __subject = input("Enter subject: ")
        __rental_price = input("Enter rental price per day: ")
        __copies = int(input("Enter number of copies: "))

        matched_data = list(x for x in self.list_of_lec_cd if x.cd_no == __cd)
        for x in matched_data:
            x.copies -= __copies
            print("CD Lent")

    def receive(self):
        __cd = input("Enter CD number: ")
        __title = input("Enter title: ")
        __subject = input("Enter subject: ")
        __rental_price = input("Enter rental price per day: ")
        __copies = int(input("Enter number of copies: "))

        matched_data = list(x for x in self.list_of_lec_cd if x.cd_no == __cd)
        for x in matched_data:
            x.copies += __copies
            print("CD received")

    def display_all(self):
        for x in self.list_of_lec_cd:
            print_info(lec_cd=x)

    def display_available(self):
        matched_data = list(x for x in self.list_of_lec_cd if x.copies > 0)
        for x in matched_data:
            print_info(lec_cd=x)

    def display_unavailable(self):
        matched_data = list(x for x in self.list_of_lec_cd if x.copies == 0)
        for x in matched_data:
            print_info(lec_cd=x)

