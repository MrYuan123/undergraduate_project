#!/usr/bin/python
# -*-coding:utf-8 -*-
import csv, math
maxR = 20

class userCF(object):
	def __init__(self):
		pass

	# main function of this section
	def userCF_alg(self,ID,userLists,movieLists):
		W = self.related_martix(movieLists)
		Rlist = self.userIIF(W,ID,userLists,movieLists)
		return Rlist

	# Calculate related_martix
	def related_martix(self,mLists):
		print("## Related matrix is generating............")
		C = dict()
		N = dict()

		for i in mLists:
			users = mLists[i]
			for u in users:
				if u in N:
					N[u]+=1
				else:
					N[u]=1

				for v in users:
					if u == v:
						continue
					else:
						if u in C:
							pass
						else:
							C[u] = dict()

						if v in C[u]:
							C[u][v] += 1/math.log(1+len(users))
						else:
							C[u][v] = 1/math.log(1 + len(users))

		W = dict()
		for u, related_users in C.items():
			if u in W:
				pass
			else:
				W[u] = dict()

			for v, cuv in related_users.items():
				W[u][v] = cuv/math.sqrt(N[u]*N[v])
				#print(W[u][v])



		for m in W:
			details = W[m]
			for n in details:
				temp = list()
				print(m)
				print(n)
				print(details[n])
				temp.append(m)
				temp.append(n)
				temp.append(details[n])
				with open("user_similarity.csv", 'a', newline='') as f:
					writer = csv.writer(f)
					writer.writerow(temp)

		print("qwwwwwwwwwwwww")
		input()
		return W

	# Genreate Recommand list.
	def userIIF(self,W,ID,uLists,mLists):
		print("## Recommand list is generating................")
		matchM = dict()
		if ID in W:
			Similar = W[ID]
			for item in Similar:
				for movieitem in uLists[item]:
					if movieitem in uLists[ID]:
						pass
					else:
						if movieitem in matchM:
							matchM[movieitem] += Similar[item]
						else:
							matchM[movieitem] = 0
							matchM[movieitem] += Similar[item]

			sortL = sorted(matchM.items(), key=lambda d: d[1], reverse=True) # turn dict into list

			if len(sortL) == 0:
				return None
			else:
				finalList = list()
				if (len(sortL) < maxR):
					for item in sortL:
						finalList.append(item[0])
				else:
					for item in sortL[:maxR]:
						# print("%s : %s"%(item[0],item[1]))
						finalList.append(item[0])
					return finalList

		else:
			return None

		return W
