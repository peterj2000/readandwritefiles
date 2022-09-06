import csv

infile = open('EmployeePay.csv' , "r")
csvfile = csv.reader(infile,delimiter=',')

next(csvfile)

for record in csvfile:
    print('ID:', record[0])
    print('First Name:', record[1])
    print('Last Name:', record[2])
    salary = float(record[3])
    bonus_per = float(record[4])
    bonus = salary*bonus_per
    total_pay = salary + bonus
    form = "{:.2f}".format(total_pay)
    print("Total Pay:" + "$ " + form)

    input()
