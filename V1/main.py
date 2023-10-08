from toursntravel import *
from tours import *

while True:
    print('----TOURS N TRAVEL-----')
    print() # empty line
    
    mainMenu = '1. Ticket Booking\n'
    mainMenu += '2. Tour Package\n'
    mainMenu += '3. Exit'
    
    print(mainMenu)
    usrChoice = int(input("Enter choice : "))
    
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