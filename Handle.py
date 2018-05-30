#!/usr/bin/python
# -*-coding:utf-8 -*-
import csv
#ratingA notice:
#It is lists, and the elements are userId, movieId and rating.

class Handle(object):
	def __init__(self):
		pass

	# User is the key.
	def users_standard(self):
		userMode = dict()
		csvfile = open("ratingsT.csv","r")
		reader = csv.reader(csvfile)

		for line in reader:
			if line[0] in userMode:
				userMode[line[0]].add(line[1])
			else:
				item=set()
				item.add(line[1])
				userMode[line[0]]=item

		return userMode

	# Movie is the key.
	def movies_standard(self):
		movieMode = dict()
		csvfile = open("ratingsT.csv","r")
		reader = csv.reader(csvfile)

		for line in reader:
			if line[1] in movieMode:
				movieMode[line[1]].add(line[0])
			else:
				item = set()
				item.add(line[0])
				movieMode[line[1]] = item
		return movieMode
