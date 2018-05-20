import csv

csvfile = open("ratingsA.csv","r")
reader = csv.reader(csvfile)

for line in reader:
    temp = [line[0],line[1],line[2]]
    with open ('ratingsB.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(temp)
