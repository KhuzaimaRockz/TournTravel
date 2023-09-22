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
    for j in range(8):
        attractions = input("Enter attractions:")
        L2.append(attractions)
    for k in range(4):
        food = input("Enter Food recommendation:")
        L2.append(food)
    mywriter2.writerow(L2)
    file2.close()

def packages():
    file = open('tours.csv', mode='r')
    myreader = csv.reader(file)
    g1 = "*"*40
    for row in myreader:
        print("=" * 100)
        one = (row[0], row[1].upper())
        string = ".".join(one)
        h = f"{string:^100s}"
        print(h)
        print('Date ', row[2], end='')
        print(' ' * 40, row[4], ' Days and')
        print('to   ', row[3], end='')
        print(' ' * 40, row[5], ' Nights')
        print(' ' * 20, 'Special Price: ', row[6], 'KWD Per Head')
        print("=" * 100)
    file.close()

packages()
#create()
#opt = int(input("Enter the package number that you would like to view: "))
#pacinfo(opt)
