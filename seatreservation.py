seatlist = {}
MAX_SEATS = 99

def print_menu():
    print (30 * "-" , "Menu", 30 * "-")
    print ("1. Add reservation")
    print ("2 Remove reservation")
    print ("3 print seat reservation list")
    print ("4 exit")
    print (67 * "-")
loop=True

while loop:
    print_menu()
    choice = input("Enter your choice [1-4]: ")
    choice=int(choice)
    if choice == 1:
        while True:
            user_input = input(f"Enter a seat number between 1 and {MAX_SEATS}: ")
            if user_input.isdigit():
                seat_num = int(user_input)
            if not user_input.isdigit():
                print(f"Enter valid seat number between 1 and {MAX_SEATS}")
                continue
            if not (1 <= seat_num <= MAX_SEATS):
                print(f"Enter valid seat number between 1 and {MAX_SEATS}")
                continue
            if seat_num in seatlist:
                print(f"Seat {seat_num} is not available.  Choose another")
                continue

            print(F"Seat {seat_num} selected,")
            name = input("What name?:  ")
            seatlist.update({seat_num:name})
            break
    elif choice == 2:
        user_input = input("ok, which seat to remove?:  ").strip()

        try:
            seat_num = int(user_input)
        except ValueError:
            print("Invalid input - please enter a valid seat nbumber.")
        else:

            if seat_num in seatlist:
                name = seatlist[seat_num]
                confirm = input(f"Seat {seat_num} is assigned to {name}.  remove it (y/n)").strip().lower()
                if confirm == 'y':
                    del seatlist[seat_num]
                    print(f"Seat {seat_num} has been removed.")
        
    elif choice == 3:
        for seat, name in seatlist.items():

            print(f"{seat:10} {name}")
        input("enter to continue")
    elif choice == 4:
        print("Goodbye")
        loop=False
    else:
        print("Wrong option buddy!")

        
