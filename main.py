#!/usr/bin/python3
# -*-coding:utf-8 -*-
import userCF,itemCF,Handle,display

class startPro(object):
	def __init__(self):
		self.Handle = Handle.Handle()
		self.userCF_alg = userCF.userCF()
		self.itemCF_alg = itemCF.itemCF()
		self.display = display.display()
		self.ID = "4"

	def mixed_alg(self, length, ulists, ilists):
		if length > 15:
			print('using userCF:')
			return ulists
		else:
			print('using itemCF:')
			return ilists


	def stack_mix(self, length, id, userList, ulists, W):
		if length < maxLength:
			return ulists
		else:
			temp = list()
			for item in ulists:
				temp.append(item[0])
			moviedict = dict()
			for item in temp:
				moviedict[item] = 0
				for movieItem in userList:
					if W[movieItem][item] > moviedict[item]:
						moviedict[item] = W[movieItem][item]
					else:
						pass
			items=moviedict.items()
			backitems=[[v[1],v[0]] for v in items]
			backitems.sort()
			return [ backitems[i][1] for i in range(0,len(backitems))]


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
		# print("ItemCF_alg section is starting.............")
		# itemCF_lists= self.itemCF_alg.itemCF_alg(self.ID,userLists,movieLists)
		# Rlists = self.mixed_alg(len(userLists[self.ID]),userCF_lists, itemCF_lists)

		# ##============= show section ===============
		print("Once:")
		self.display.display_movies(userLists[self.ID])
		print("Recommand:")
		self.display.display_movies(userCF_lists)
		print(len(userLists[self.ID]))
		print(len(userCF_lists))

if __name__ == "__main__":
	s = startPro()
	s.start_pro()
