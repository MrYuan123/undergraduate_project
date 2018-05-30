#!/usr/bin/python
# -*-coding:utf-8 -*-
import csv

class display(object):
    def __init__(self):
        pass

    def display_movies(self, Ids):
        # for item in Ids:
        #     print(item)
        csvfile = open("movies.csv","r")
        reader = csv.reader(csvfile)

        for item in reader:
            if item[0] in Ids:
                print("%s : %s : %s"%(item[0],item[1],item[2]))

        return
