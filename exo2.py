# Exercise 2: Ticket Purchase System

client_name = input("What's your name sir ? ")

if client_name == "VIP":
    print("Enjoy Sir, your seat is in the front.")
else:
    nb_tickets = int(input("How many tickets for Barbie movie? "))
    cost = nb_tickets * 15.5
    print(f"That would be {cost}$ please.")
