#!/usr/bin/python3
# -*-coding:utf-8 -*-
import math, numpy,csv,traceback,pymysql
MAXmovies = 20

class itemCF(object):
    def __init__(self):
        pass

    def get_list(self,movieN):
        return_list = list()
        # return_list = ['4428', '112582', '104321', '43351', '25940', '43910', '47894', '114464', '70418', '99089', '98441', '141749', '25795', '26323', '25904', '4684', '44073', '101904', '34364','1152', '91582', '109740', '110453', '7922', '8331', '8261', '4606', '5088', '8388', '93700']
        try:
            db = pymysql.connect("localhost","root","Yyk19951006+","undergraduate" )
            db.set_charset('utf8')
            cursor = db.cursor()
        except Exception:
            traceback.print_exc()
            return "connection fail!"
            input()

        sql_command = 'select * from item_similarity where user1 ='
        for item in movieN:
            sql_command = sql_command + item + ' or user1 = '

        sql_command = sql_command[:-12]
        sql_command = sql_command + ' order by simi desc;'
        print(sql_command)

        try:
            cursor.execute(sql_command)
            results = cursor.fetchall()
            results = results[:30]
            for item in results:
                return_list.append(item[1])
                print(item)

            print(return_list)
                # for item in results:
                #     temp = list()
                #     print('movieID1:'+item[0])
                #     print('movieID2:' + item[1])
                #     print('similarity: ' + item[2])
                #     temp.append(item[0])
                #     temp.append(item[1])
                #     temp.append(item[2])
                #     with open ('temp.csv','a', newline='') as f:
                #         writer = csv.writer(f)
                #         writer.writerow(temp)
        except:
            print("sort fail!")
            input()

        return return_list

    def itemCF_alg(self,ID,uLists, mLists):
        movieN = uLists[ID]
        similarity_list = self.get_list(movieN)

        # W = self.itemSimilarity(uLists,mLists)
        # with open("similarity.csv","w",newline='') as f:
        #     writer = csv.writer(f)
        #     for u in W:
        #         for v in W[u]:
        #             temp = list()
        #             temp.append(u)
        #             temp.append(v)
        #             temp.append(W[u][v])
        #             writer.writerow(temp)
        #             print("%s and %s : %s"%(u,v,W[u][v]))

        # numpy.savetxt('similarity.csv', W, delimiter = ',')

        # with open("similarity.csv","w",newline='') as f:
        #     writer = csv.writer(f)
        #     for item in W:
        #         temp = dict()
        #         temp[item] = W[item]
        #         print(temp)
        #         writer.writerow(temp)

        return similarity_list

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

        # numpy.savetxt('new.csv', C, delimiter = ',')
        print("cal finish!")
        input()
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
