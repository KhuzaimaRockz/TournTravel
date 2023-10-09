from toursntravel import *
from tours import *

while True:
    print('*' * 100)
    tprint('TravelOn Tours'.center(25))
    print('*' * 100)
    print('-' * 100)
    print('=' * 100)
    print(f"{'1. Ticket Booking':^100s}")
    print(f"{'2. Tour Packages':^100s}")
    print(f"{'3. Exit':^100s}")
    print('=' * 100)
    print('-' * 100)

    usrChoice = int(input("Enter your choice : "))
    if usrChoice == 1:
        ticket()
        continue
    elif usrChoice == 2:
        tours()
        continue
    elif usrChoice == 420:
        print("shush.")
    else:
        break
    #