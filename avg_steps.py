import csv

infile = open("steps.csv", 'r')
outfile = open('avg_steps.csv',"w")

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)


mon = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
count = 1

outfile.write('Month, Average Steps Taken\n')
for x in csvfile:
    #print(i)
    if float(x[0])!=count:
        count-=1
        average =(a/i)
        average=format(average,',.2f')
        print(mon[count]+', '+str(average))
        outfile.write(mon[count]+', '+str(average)+'\n')
        count+=2
        i=0
        a=0
    if float(x[0])==count:
        a+=float(x[1])
        i+=1


