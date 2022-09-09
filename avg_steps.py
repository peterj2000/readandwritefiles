import csv

infile = open("steps.csv", 'r')
outfile = open('avg_steps.csv',"w")

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)


prof_b = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
count = 1

outfile.write('Month, Avg Steps Taken\n')
for x in csvfile:
    #print(i)
    if float(x[0])!=count:
        count-=1
        avg=(a/i)
        avg=format(avg,',.2f')
        print(prof_b[count]+', '+str(avg))
        outfile.write(prof_b[count]+', '+str(avg)+'\n')
        count+=2
        i=0
        a=0
    if float(x[0])==count:
        a+=float(x[1])
        i+=1


