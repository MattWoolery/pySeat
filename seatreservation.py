seatlist = {}

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
        seat = input("Which Seat?: ").lower()
        while seat in seatlist:  # Check if the seat is already reserved
            print(f"Seat {seat} is already occupied. Please choose another seat.")
            seat = input("Which Seat?: ").lower()
        name = input("What name?:  ")
        seatlist.update({seat:name})
    elif choice == 2:
        seat= input("ok, which seat to remove?:  ").lower()
        if seat in seatlist:
            del seatlist[seat]
            print(f"Seat {seat} has been removed.")
        seatlist.pop(seat)
    elif choice == 3:
        for seat, name in seatlist.items():
            print(f"{seat:10} {name}")
        input("enter to continue")
    elif choice == 4:
        print("Goodbye")
        loop=False
    else:
        print("Wrong option buddy!")

        
