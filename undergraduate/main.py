#!/usr/bin/python
# -*-coding:utf-8 -*-
import userCF,itemCF,Handle,display

class startPro(object):
	def __init__(self):
		self.Handle = Handle.Handle()
		self.userCF_alg = userCF.userCF()
		self.itemCF_alg = itemCF.itemCF()
		self.display = display.display()

	def start_pro(self):
		#============= data standard ==============
		# ========= movie
		print("Movie list is generating...........")
		movieLists = self.Handle.movies_standard()

		# ========= user
		print("User list is generating.............")
		userLists = self.Handle.users_standard()

		#============== user alg section ================
		# print("UserCF_Alg section is starting.............")
		# ID = "1"
		# Rlist = self.userCF_alg.userCF_alg(ID,userLists,movieLists)

		#============== item alg section ================
		print("ItemCF_alg section is starting.............")
		ID = "2"
		Rlist = self.itemCF_alg.itemCF_alg(ID,userLists,movieLists)

		##============= show section ===============
		# print("Once:")
		# self.display.display_movies(userLists[ID])
		# print("Recommand:")
		# self.display.display_movies(Rlist)

if __name__ == "__main__":
	s = startPro()
	s.start_pro()
