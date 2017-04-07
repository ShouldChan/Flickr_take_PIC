# coding:utf-8
import time
import operator
import random

# here to change the city name, so u don't have to edit the codes below
CITY_NAME = 'Buda'

data_dir = "./data/"
result_dir = "./result/"
pic_dir = "./pic/"
city_dir = "./city/"
des_dir = "./des/"
hyb_dir = "./hybrid/"
rand_dir = "./random/"
lost_dir= "./lost/"

# 读取无效图片列表
t0 = time.time()
lost_set = set()
with open(lost_dir + CITY_NAME +'_LOST.txt','r') as readLost:
	lines = readLost.readlines()
	for line in lines:
		temp = line.strip()
		lost = temp + '.jpg'
		lost_set.add(lost)
print lost_set
print 'read lost over:', time.time() - t0

# 读取POI点和对应的photoID
t1 = time.time()
pho_poi_list = []
poi_set = set()
with open(hyb_dir + CITY_NAME + '_Info_hybrid.txt','r') as readPOI:
    lines = readPOI.readlines()
    for line in lines:
        tempData = line.strip().split('\t')
        photoID, jpgName, poiID = tempData[0], tempData[1], int(tempData[2])
        if jpgName not in lost_set:
	        pho_poi_list.append([photoID, jpgName, poiID])
	        poi_set.add(poiID)
	        # pho_poi_dict[photoID] = poiID
print 'read hybrid over: ', time.time()-t1

# 随机每个poi点取20个
random_list = []

t2 = time.time()
for iteration in poi_set:
    temp_list = []
    for [photoID, jpgName, poiID] in pho_poi_list:
        if poiID == iteration:
            temp_list.append([photoID, jpgName, poiID])
    random.shuffle(temp_list)
    random_list.extend(temp_list[:20])

random_list.sort(key=operator.itemgetter(2),reverse=False)
print random_list
print 'select random over...', time.time() - t2

# 写入文件
t3 = time.time()

fwrite = open(rand_dir + CITY_NAME + '_Random_list.txt','a+')
for [photoID, jpgName, poiID] in random_list:
    fwrite.write(str(photoID)+'\t'+str(jpgName)+'\t'+str(poiID)+'\n')
fwrite.close()
print 'write over', time.time() - t3