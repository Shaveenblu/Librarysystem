from bookfunction import BookFunction
from educationaldvdfunction import DVDFunction
from magazinefunction import MagazineFunction
from LectureCD import LectureCDFunction

#objects creating varibles could be accessed with the help of object name
bookfunc = BookFunction()
dvdfunc = DVDFunction()
magfunc = MagazineFunction()
lec_cdfunc = LectureCDFunction()


def mainmenu():
    print("Main menu")
    print("")
    print("1 - Books")
    print("2 - Magazine")
    print("3 - Educational DVD")
    print("4 - Lecture CD")
    print("5 - Quit")

    selected_resource = 1
    
    while selected_resource > 0:
        try:
            selected_resource = int(input("Please select your option: "))
        except ValueError:
            print("Invalid Entry.")
            mainmenu()

        if selected_resource == 0:
            print("Thank you for using university library system.")
            quit()
        elif selected_resource == 1:
            function_name = bookfunc
            submenu_book(function_name, "Book")
            break
        elif selected_resource == 2:
            function_name = magfunc
            submenu_magazine(function_name, "Magazine")
            break
        elif selected_resource == 3:
            function_name = dvdfunc
            submenu_dvd(function_name, "Educational DVD")
            break
        elif selected_resource == 4:
            function_name = lec_cdfunc
            submenu_cd(function_name, "Lecture CD")
            break
        elif selected_resource == 5:
            print("Thank you")
            quit()
        else:
            print("Invalid Selection in menu.")


def submenu_book(bookfunc,selected_resource):
    selected_operation = 1
    while selected_operation > 0:
        print("Please select a number from the menu")
        print("--------------------------------")
        print(f"1 - Add a {selected_resource}")
        print(f"2 - Remove a {selected_resource}")
        print(f"3 - Display Available {selected_resource}s")
        print(f"4 - Display Unavailable {selected_resource}s")
        print(f"5 - Display All {selected_resource}s")
        print(f"6 - Lend {selected_resource}")
        print(f"7 - Receive {selected_resource}")
        print("8 - Back to Main Menu")
        print("9 - Quit")
        selected_operation = int(input("Please type a number from the menu: "))

        if selected_operation == 1:
            bookfunc.add()
        elif selected_operation == 2:
            bookfunc.remove()
        elif selected_operation == 3:
            bookfunc.display_available()
        elif selected_operation == 4:
            bookfunc.display_unavailable()
        elif selected_operation == 5:
            bookfunc.display_all()
        elif selected_operation == 6:
            bookfunc.lend()
        elif selected_operation == 7:
            bookfunc.receive()
        elif selected_operation == 8:
            mainmenu()
        elif selected_operation == 9:
            print("Thank you for using university library system.")
            quit()
        else:
            print("invalid selection")

        if 1<= selected_operation <= 7:
            input("Press any key    ")


def submenu_magazine(magfunc, selected_resource):
    selected_operation = 2
    while selected_operation > 0:
        print("Please select a number from the menu")
        print("--------------------------------")
        print(f"1 - Add a {selected_resource}")
        print(f"2 - Remove a {selected_resource}")
        print(f"3 - Display Available {selected_resource}s")
        print(f"4 - Display Unavailable {selected_resource}s")
        print(f"5 - Display All {selected_resource}s")
        print(f"6 - Lend {selected_resource}")
        print(f"7 - Receive {selected_resource}")
        print("8 - Back to Main Menu")
        print("9 - Quit")
        selected_operation = int(input("Please type a number from the menu: "))

        if selected_operation == 1:
            magfunc.add()
        elif selected_operation == 2:
            magfunc.remove()
        elif selected_operation == 3:
            magfunc.display_all()
        elif selected_operation == 4:
            magfunc.display_unavailable()
        elif selected_operation == 5:
            magfunc.display_all()
        elif selected_operation == 6:
            magfunc.lend()
        elif selected_operation == 7:
            magfunc.receive()
        elif selected_operation == 8:
            mainmenu()
        elif selected_operation == 9:
            print("Thank you for using university library system.")
            quit()
        else:
            print("invalid selection")

        if 1 <= selected_operation <= 7:
            input("Press any key       ")

def submenu_dvd(dvdfunc,selected_resource):
    selected_operation = 3
    while selected_operation > 0:
        print("Please select a number from the menu")
        print("--------------------------------")
        print(f"1 - Add a {selected_resource}")
        print(f"2 - Remove a {selected_resource}")
        print(f"3 - Display Available {selected_resource}s")
        print(f"4 - Display Unavailable {selected_resource}s")
        print(f"5 - Display All {selected_resource}s")
        print(f"6 - Lend {selected_resource}")
        print(f"7 - Receive {selected_resource}")
        print("8 - Back to Main Menu")
        print("9 - Quit")
        selected_operation = int(input("Please type a number from the menu: "))

        if selected_operation == 1:
            dvdfunc.add()
        elif selected_operation == 2:
            dvdfunc.remove()
        elif selected_operation == 3:
            dvdfunc.display_all()
        elif selected_operation == 4:
            dvdfunc.display_unavailable()
        elif selected_operation == 5:
            dvdfunc.display_all()
        elif selected_operation == 6:
            dvdfunc.lend()
        elif selected_operation == 7:
            dvdfunc.receive()
        elif selected_operation ==8:
            mainmenu()
        elif selected_operation == 9:
            print("Thank you for using university library system.")
            quit()
        else:
            print("invalid selection")

        if 1 <= selected_operation <= 7:
            input("Press any key    ")

def submenu_cd(lec_cdfunc, selected_resource):
    selected_operation = 4
    while selected_operation > 0:
        print("Please select a number from the menu")
        print("--------------------------------")
        print(f"1 - Add a {selected_resource}")
        print(f"2 - Remove a {selected_resource}")
        print(f"3 - Display Available {selected_resource}")
        print(f"4 - Display Unavailable {selected_resource}")
        print(f"5 - Display All {selected_resource}")
        print(f"6 - Lend {selected_resource}")
        print(f"7 - Receive {selected_resource}")
        print("8 - Back to Main Menu")
        print("9 - Quit")
        selected_operation = int(input("Please type a number from the menu: "))

        if selected_operation == 1:
            lec_cdfunc.add()
        elif selected_operation == 2:
            lec_cdfunc.remove()
        elif selected_operation == 3:
            lec_cdfunc.display_all()
        elif selected_operation == 4:
            lec_cdfunc.display_unavailable()
        elif selected_operation == 5:
            lec_cdfunc.display_all()
        elif selected_operation == 6:
            lec_cdfunc.lend()
        elif selected_operation == 7:
            lec_cdfunc.receive()
        elif selected_operation == 8:
            mainmenu()
        elif selected_operation == 9:
            print("Thank you for using university library system.")
            quit()
        else:
            print("invalid selection")

        if 1 <= selected_operation <= 7:
            input("Press any key       ")


#Prints in the begining
print("")
print(" WELCOME TO University LIBRARY SYSTEM ")
print("")
print()
mainmenu()
