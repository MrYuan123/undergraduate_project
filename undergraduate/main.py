#!/usr/bin/python3
# -*-coding:utf-8 -*-
import userCF,itemCF,Handle,display

class startPro(object):
	def __init__(self):
		self.Handle = Handle.Handle()
		self.userCF_alg = userCF.userCF()
		self.itemCF_alg = itemCF.itemCF()
		self.display = display.display()
		self.ID = "671"

	def mixed_alg(self, length, ulists,ilists):
		if length > 10:
			print('using userCF:')
			return ulists
		else:
			print('using itemCF:')
			return ilists

	def start_pro(self):
		#============= data standard ==============
		# ========= movie
		print("Movie list is generating...........")
		movieLists = self.Handle.movies_standard()

		# ========= user
		print("User list is generating.............")
		userLists = self.Handle.users_standard()


		#============== user alg section ================
		print("UserCF_Alg section is starting.............")
		userCF_lists = self.userCF_alg.userCF_alg(self.ID,userLists,movieLists)

		#============== item alg section ================
		print("ItemCF_alg section is starting.............")
		itemCF_lists= self.itemCF_alg.itemCF_alg(self.ID,userLists,movieLists)
		Rlist = self.mixed_alg(len(userLists[self.ID]),userCF_lists, itemCF_lists)

		##============= show section ===============
		print("Once:")
		self.display.display_movies(userLists[self.ID])
		print("Recommand:")
		self.display.display_movies(Rlist)

if __name__ == "__main__":
	s = startPro()
	s.start_pro()
