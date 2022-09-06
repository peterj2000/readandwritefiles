import csv
infile = open("customers.csv" , "r")
outfile = open('customer_country.csv' , "w")

csvfile = csv.reader(infile, delimiter=',')

next(csvfile) #this will skip the first row

for record in csvfile:
    print("Name:" + record[1] +''+ record[2] + ',' + record[4])

    input()