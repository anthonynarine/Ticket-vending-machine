import tickets


def ask():
    print ("Welcome to Julia's Drugstore")

    while True:
        print ("[P] - Perfume\n[M] - Medicine\n[C] - Cosmetics")
        try:
            my_product = input ("Choose your Product: ").upper()
            ["P", "M", "C"].index(my_product)
        except ValueError:
            print("That is not a valis option")
        else:
            break
    tickets.decorator(my_product)


def start():
    
    while True:
        ask()
        try:
            another_ticket = input ("Do you want another ticket: [Y] [N] ").upper()
            ["Y", "N"].index(another_ticket)
        except ValueError:
            print("Not a valid Option")
        else:
            if another_ticket == "N":
                print ("Thanks for visiting Julia's Drugstore")
                break

start()


