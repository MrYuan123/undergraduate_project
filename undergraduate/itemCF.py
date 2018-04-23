#!/usr/bin/python3
# -*-coding:utf-8 -*-
import math, numpy,csv
MAXmovies = 20

class itemCF(object):
    def __init__(self):
        pass

    def itemCF_alg(self,ID,uLists, mLists):
        W = self.itemSimilarity(uLists,mLists)
        with open("similarity.csv","w",newline='') as f:
            writer = csv.writer(f)
            for u in W:
                for v in W[u]:
                    temp = list()
                    temp.append(u)
                    temp.append(v)
                    temp.append(W[u][v])
                    writer.writerow(temp)
                    print("%s and %s : %s"%(u,v,W[u][v]))

        # numpy.savetxt('similarity.csv', W, delimiter = ',')

        # with open("similarity.csv","w",newline='') as f:
        #     writer = csv.writer(f)
        #     for item in W:
        #         temp = dict()
        #         temp[item] = W[item]
        #         print(temp)
        #         writer.writerow(temp)

        return

        # for u in W:
        #     for v in W[u]:
        #         print("%s and %s : %s"%(u,v,W[u][v]))
        #
        # rank =  dict()
        # IDitems = uLists[ID]
        # for item in IDitems:
        #     if len(W[item]) < MAXmovies:
        #         rank.update(W[item])
        #     else:
        #         pass
        #
        # return W

    def itemSimilarity(self, uLists, mLists):
        C = dict() # matrix
        #print(len(mLists["2709"]))

        for i in uLists:
            item = uLists[i]
            for u in item:
                for v in item:
                    if u == v:
                        pass
                    else:
                        if u in C:
                            if v in C[u]:
                                C[u][v] += 1
                            else:
                                C[u][v] = 1
                        else:
                            if v in C:
                                if u in C[v]:
                                    C[v][u] += 1
                                else:
                                    C[v][u] = 1
                            else:
                                C[v] = dict()
                                C[v][u] = 1


        for m in C:
            for n in C[m]:
                C[m][n] = 1/math.log(1 + C[m][n])/math.sqrt(len(mLists[m])*len(mLists[n]))
        return C

        # for i in uLists:
        #     items = uLists[i]
        #     for u in items:
        #         for v in items:
        #             if u == v:
        #                 continue
        #             else:
        #                 if u in C:
        #                     pass
        #                 else:
        #                     C[u] = dict()
        #
        #                 if v in C[u]:
        #                     C[u][v] += 1
        #                 else:
        #                     C[u][v] = 1
        # W = dict()
        # for i,related_items in C.items():
        #         for j, cij in related_items.items():
        #                 print(cij)
        #                 print(len(mLists[i]))
        #                 print(len(mLists[j]))
        #                 W[u][v] = cij / math.sqrt(len(mLists[i])*len(mLists[j]))
        # return W
