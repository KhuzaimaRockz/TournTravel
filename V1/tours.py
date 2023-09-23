# we use csv or binary file and we will have existing tour offers by travelon
# and then we can display the option for show, update, delete, ex
import csv

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
    c = 0
    with open('tours.csv', "r") as f:
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
    print("8 Attractions to be entered")
    for j in range(8):
        attractions = input("Enter attractions:")
        L2.append(attractions)
    print("4 Food recommendations to be entered")
    for k in range(4):
        food = input("Enter Food recommendation:")
        L2.append(food)
    mywriter2.writerow(L2)
    file2.close()

def packages():
    file = open('tours.csv', mode='r')
    myreader = csv.reader(file)
    g3=" "*3
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

        #print(' ' * 40, row[4], ' Days and')
        #print('to   ', row[3], end='')
        #print(' ' * 40, row[5], ' Nights')
        print('-' * 30, end='')
        one2 = (row[6])
        string2 = "".join(one2)
        print(f"{' Special Price: '}{string2:^10s}{'KWD Per Head '}", end='')
        print(f"{'-' * 30:^20}")

        print("=" * 100)
    file.close()
def pacinfo(opt):
    with open('pacinfo.csv', "r") as f:
        reader = csv.reader(f)
        try:
            for i in range(opt):
                row = next(reader)
            print(row[0])
            print(row[1])
            print(row[2])
        except StopIteration:
            print("The row does not exist.")

packages()
#create()
#opt = int(input("Enter the package number that you would like to view: "))
#pacinfo(opt)
