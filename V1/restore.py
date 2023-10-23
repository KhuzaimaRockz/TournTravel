import csv
l=[[1,'Georgia','30-12-2023','03-01-2024','5','4','248'], [2,'india','07-11-2023','13-11-2023','7','6','225'], [3,'Azerbaijan','26-12-2023','30-12-2023','5','4','182']]
with open('tours.csv', 'w', newline='') as f:
    writer=csv.writer(f)
    for lrow in l:
        writer.writerow(lrow)