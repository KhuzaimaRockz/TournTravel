#we use csv or binary file and we will have existing tour offers by travelon
#and then we can display the option for show, update, delete, ex
import csv

def create():
    file=open('tours.csv',mode='w',newline='')
    mywriter=csv.writer(file,delimiter=',')
    L=[]
    for i in range(1):
        dfrom=input('enter from date:')
        dto=input('enter to date:')
        country=input('enter country name:')
        nonights=int(input('enter no. of nights:'))
        noday=int(input('enter no.of days:'))
        paprice=float(input('enter overall cost:'))
        L=([dfrom,dto,country,nonights,noday,paprice])
    mywriter.writerow(L)
    file.close()
def display():
    file=open('tours.csv',mode='r')
    myreader=csv.reader(file)
    for row in myreader:
        print('from date=',row[0])
        print('to date=', row[1])
        print('country=', row[2])
        print('no. of nights=', row[3])
        print('no. of days=', row[4])
        print('price per head=', row[5])
    file.close()

display()



