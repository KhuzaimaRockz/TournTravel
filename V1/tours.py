# we use csv or binary file and we will have existing tour offers by travelon
# and then we can display the option for show, update, delete, ex
import csv
from art import *
from error import error_handle
import os

def tours():
    g2=" "*2
    g3=" "*3
    # display 3 country packages (Georgia, Azerbaijan, Turkiye): (things to display for options)
    # country
    # per person price
    # days and nights
    # date (from and to)
    # (after user chooses a package to view more info):
    # attractions (8 places)
    # food recommendations (4)
    # inclusions
    # create your own package
    # edit a package
    # delete a package
    # exit

    def create():
        with open('tours.csv', "r") as f:
            c = 0
            reader = csv.reader(f)
            last_row = next(reader)
            for row in reader:
                last_row = row

            if last_row:
                c = int(last_row[0])
            else:
                return None
        file = open('tours.csv', mode='a', newline='')
        mywriter = csv.writer(file, delimiter=',')
        L = []
        for i in range(1):
            c += 1
            country = input('enter country name:')
            dfrom = input('enter from date:')
            dto = input('enter to date:')
            nonights = int(input('enter no. of nights:'))
            noday = int(input('enter no.of days:'))
            paprice = float(input('enter overall cost:'))
            L = ([c, country, dfrom, dto, nonights, noday, paprice])
        mywriter.writerow(L)
        file.close()
        file2 = open('pacinfo.csv',mode='a',newline='')
        mywriter2 = csv.writer(file2, delimiter=',')
        L2 = []
        print('-' * 100)
        print(f"{'Inclusions will be offered by TravelOn Tours which are fixed for every trip!':^100s}")
        print(f"{'8 Attractions to be entered':^100s}")
        print('-' * 100)
        for j in range(8):
            attractions = input("Enter attractions:")
            L2.append(attractions)
        print('-' * 100)
        print(f"{'4 Food recommendations to be entered':^100s}")
        print('-' * 100)
        for k in range(4):
            food = input("Enter Food recommendation:")
            L2.append(food)
        mywriter2.writerow(L2)
        file2.close()

    def packages():
        file = open('tours.csv', mode='r')
        myreader = csv.reader(file)
        g3=" "*3
        print('*' * 100)
        tprint('TravelOn Tours'.center(25))
        print('*' * 100)
        print()
        for row in myreader:
            print("=" * 100)
            print('*'*37, end='')
            one = (row[0], row[1].upper())
            string = ".".join(one)
            print(f"{string:^26s}", end='')
            print(f"{'*' * 37:^20}")
            print('' * 30, end='')
            print(f"{'Date':^18s}{g3}{'To':^16s}", end='')
            print(' ' * 26, end='')
            print(f"{'Days':^17s}{g3}{'Nights':^17s}")
            print('' * 30, end='')
            print(f"{row[2]:^18s}{g3}{row[3]:^16s}", end='')
            print(' ' * 26, end='')
            print(f"{row[4]:^17s}{g3}{row[5]:^17s}")
            print('-' * 30, end='')
            one2 = (row[6])
            string2 = "".join(one2)
            print(f"{' Special Price: '}{string2:^10s}{'KWD Per Head '}", end='')
            print(f"{'-' * 30:^20}")
            print("=" * 100)
        file.close()
        
    def pacinfo(optpac):
        print('*' * 100)
        tprint('TravelOn Tours'.center(25))
        print('*' * 100)
        print()
        with open('pacinfo.csv', "r") as f:
            reader = csv.reader(f)
            g26= ' ' * 26

            try:
                for i in range(optpac):
                    row = next(reader)
                print("=" * 100)
                print('*' * 37, end='')
                print(f"{'ATTRACTIONS':^26s}", end='')
                print(f"{'*' * 37:^20}")
                print(f"{row[0]:^37s}{g26}{row[1]:^37s}")
                print(f"{row[2]:^37s}{g26}{row[3]:^37s}")
                print(f"{row[4]:^37s}{g26}{row[5]:^37s}")
                print(f"{row[6]:^37s}{g26}{row[7]:^37s}")
                print("-" * 100)
                print('*' * 37, end='')
                print(f"{'FOOD RECOMMENDATIONS':^26s}", end='')
                print(f"{'*' * 37:^20}")
                print(f"{row[8]:^37s}{g26}{row[9]:^37s}")
                print(f"{row[10]:^37s}{g26}{row[11]:^37s}")
                print("-" * 100)
                print('*' * 37, end='')
                print(f"{'INCLUSIONS':^26s}", end='')
                print(f"{'*' * 37:^20}")
                print(f"{'Hotel':^37s}{g26}{'Breakfast':^37s}")
                print(f"{'Guide':^37s}{g26}{'Private Car':^37s}")
                print(f"{'Sim Card':^37s}{g26}{'Water':^37s}")
                print(f"{'Entrance Tickets':^37s}{g26}{'Airport Transfer':^37s}")
                print(f"{'Insurance':^37s}{g26}{'Air Tickets':^37s}")
                print("=" * 100)
                input("Press [ENTER] to continue.")
            except StopIteration:
                print('*' * 100)
                tprint('TravelOn Tours'.center(25))
                print('*' * 100)
                print()
                print("The row does not exist.")
    def update():
        packages()
        pack = int(input("Enter the package you want to modify: "))
        with open("tours.csv", 'r', newline='') as f:
            reader = csv.reader(f)
            tempdata = []
            for row in reader:
                tempdata.append(row)

        with open("tours.csv", 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            for row in tempdata:
                if pack == int(row[0]):
                    ncountry = input('Enter country name: ')
                    ndfrom = input('Enter from date: ')
                    ndto = input('Enter to date: ')
                    nnonights = int(input('Enter no. of nights: '))
                    nnoday = int(input('Enter no. of days: '))
                    npaprice = float(input('Enter overall cost: '))

                    row[1] = ncountry
                    row[2] = ndfrom
                    row[3] = ndto
                    row[5] = nnonights
                    row[4] = nnoday
                    row[6] = npaprice
                writer.writerow(row)
        with open("pacinfo.csv", 'r', newline='') as f:
            reader = csv.reader(f)
            tempdata = []
            for row in reader:
                tempdata.append(row)
        with open("pacinfo.csv", 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            for row in tempdata:
                L2 = []
                print('-' * 100)
                print(f"{'Inclusions will be offered by TravelOn Tours which are fixed for every trip!':^100s}")
                print(f"{'8 Attractions to be entered':^100s}")
                print('-' * 100)
                for j in range(8):
                    attractions = input("Enter attractions:")
                    L2.append(attractions)
                print('-' * 100)
                print(f"{'4 Food recommendations to be entered':^100s}")
                print('-' * 100)
                for k in range(4):
                    food = input("Enter Food recommendation:")
                    L2.append(food)
            f.seek(pack)
            writer.writerow(L2)
    def delete():
        f = open('tours.csv', 'r', newline='')
        reader = csv.reader(f)

        usrDel = int(input('Enter Package to delete data for: '))

        flag = False
        tempRows = []

        for row in reader:
            if int(row[0]) == usrDel:
                flag = True
            else:
                tempRows.append(row)

        if flag:
            f.close()
            f = open('tours.csv', 'w', newline='')
            writer = csv.writer(f)
            writer.writerows(tempRows)
            f.close()
            print('---Deleted successfully.')

        else:
            print('Error: City not found for deletion, hence not deleted.')
        f.close()
        f = open('tours.csv', 'r+', newline='')
        reader = csv.reader(f)
        writer = csv.writer(f)

        c = 1
        L = []
        for row in reader:
            row[0] = c
            c+=1
            L.append(row)
        f.seek(0)
        writer.writerows(L)
        f.close()



    #calling the functions:
    print('*' * 100)
    tprint('TravelOn Tours'.center(25))
    print('*' * 100)
    while True:
        print('=' * 100)
        print(f"{'1. Existing Packages':^100s}")
        print(f"{'2. Create A Package':^100s}")
        print(f"{'3. Update A Package':^100s}")
        print(f"{'4. Delete A Package':^100s}")
        print(f"{'5. Go Back To Main Menu':^100s}")
        print('=' * 100)
        opt = input("Enter Your Choice: ")
        if opt not in ['1', '2', '3', '4', '5']:
            input("Error: Invalid input (ENTER): ")
            error_handle(101)
        else:
            break
    if opt == '1':
        packages()
        optpac = int(input("Enter A Package For More Info: "))
        pacinfo(optpac)
    elif opt == '2':
        create()
        douopt = input("Do You Want To See New Packages? (Y/N): ")
        if douopt not in ['Y','y','N','n']:
            input("Error: Invalid input (ENTER): ")
            error_handle(101)
        elif douopt in ['Y', 'y']:
            packages()
    elif opt == '3':
        update()
        douopt = input("Do You Want To See Updated Packages? (Y/N): ")
        if douopt not in ['Y', 'y', 'N', 'n']:
            input("Error: Invalid input (ENTER): ")
            error_handle(101)
        elif douopt in ['Y', 'y']:
            packages()
    elif opt == '4':
        delete()
        douopt = input("Do You Want To See Older Packages? (Y/N): ")
        if douopt not in ['Y', 'y', 'N', 'n']:
            input("Error: Invalid input (ENTER): ")
            error_handle(101)
        elif douopt in ['Y', 'y']:
            packages()