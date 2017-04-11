# coding:utf-8
import time
import operator
import random

# here to change the city name, so u don't have to edit the codes below
# CITY_NAME = 'Buda'

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
global Toro_num
Toro_num = 0
with open(data_dir + 'yfcc100m_places.txt','r') as readCity:
	lines = readCity.readlines()
	for line in lines:
		temp = line.strip().split('\t')
		photoID, cityStr = temp[0], temp[1]
        print cityStr
        if cityStr.find('Toronto') == 1:
            Toro_num += 1
            continue
        else if cityStr != Null and cityStr.find('Toronto') == -1:
            continue
        if cityStr == Null:
            Toro_num += 1


print 'read lost over:', time.time() - t0
