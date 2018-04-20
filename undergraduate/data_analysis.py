#!/usr/bin/python
# -*-coding:utf-8-*-
import csv

def ratings_data():
	totalR=0
	totalW=0
	with open("ratingsA.csv","w",newline='') as f:
		writer = csv.writer(f)
		reader = csv.reader(open('ratings.csv', 'r'))
		for line in reader:
			totalR+=1
			tem= line
			tem.pop()
			writer.writerow(tem)
			totalW+=1
			print ("%s"%(tem))
			print (totalR)
	return 0

def movies_data():
    return 0

def tags_data():
	totalR=0
	totalW=0
	with open("tagsA.csv","w",newline='') as f:
		writer = csv.writer(f)
		reader = csv.reader(open('tags.csv', 'r'))
		for line in reader:
			totalR+=1
			tem= line
			tem.pop()
			writer.writerow(tem)
			totalW+=1
			print ("%s"%(tem)+"%d"%(totalW))
		print (totalR)
	return 0


if __name__ == "__main__":
    ratings_data()
    print("rating finish!")
    tags_data()
    print("tags finish!")
