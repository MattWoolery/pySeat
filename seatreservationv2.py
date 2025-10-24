MAX_SEATS = 99
loop = True
while loop:
    print_menu()
    choice = input("Enter your choice [1-4]: ")
    choice=int(choice)
    if choice == 1:
        seat = None
        while True:
            try:
                seat = int(input(f"Which Seat? (1-{MAX_SEATS}): "))
                if 1 <= seat <= MAX_SEATS:
                    break
                else:
                    print(f"Please enter a number between 1 and {MAX_SEATS}.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        while seat in seatlist:  
            print(f"Seat {seat} is already occupied. Please choose another seat.")
            try:
                seat = int(input(f"Which Seat? (1-{MAX_SEATS}): "))
                if 1 <= seat <= MAX_SEATS:
                    break
                else:
                    print(f"Please enter a number between 1 and {MAX_SEATS}.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        name = input("What name?:  ")
        seatlist.update({seat:name})
    elif choice == 2:
        seat= None
        while True:
            try:
                seat = int(input(f"Which Seat to remove? (1-{MAX_SEATS}): "))
                if 1 <= seat <= MAX_SEATS:
                    break
                else:
                    print(f"Please enter a number between 1 and {MAX_SEATS}.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        if seat in seatlist:
            del seatlist[seat] 
            print(f"Seat {seat} has been removed.")
        else:
            print(f"Seat {seat} is not occupied.")
    elif choice == 3:
        for seat, name in seatlist.items():
            print(f"{seat:4} {name}")
        input("Press Enter to continue...")
    elif choice == 4:
        print("Goodbye")
        loop=False
    else:
        print("Wrong option buddy!")
