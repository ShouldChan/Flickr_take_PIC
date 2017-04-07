# coding: utf-8

import csv
import time

CITY_NAME = 'Toro'

data_dir = "./data/"
result_dir = "./result/"
pic_dir = "./pic/"
city_dir = "./city/"
des_dir = "./des/"
vec_dir = "./vector/"


t1=time.time()

fwrite = open(vec_dir+'Format_vector_'+ CITY_NAME +'.txt','a+')

with open(vec_dir + 'vector_' + CITY_NAME + '.txt','r') as readVec:
	lines = readVec.readlines()
	count = 1
	for line in lines:
		temp1 = line.replace('[','')
		temp2 = temp1.replace(']','')
		temp3 = temp2.replace(',','\t');
		jpg_name = str(count)+'.jpg'
		print count
		count += 1
		# print temp3
		# tempData = line.strip().split(',')
		# array = []
		# for i in range(2048):
		# 	if i == 0:
		# 		array[0] = tempData[0].lstrip('[')
		# 	else if i==2047:
		# 		array[2247] = tempData[2247].rstrip(']')
		# 	else:
		# 		array[i] = tempData[i]
		fwrite.write(str(jpg_name)+'\t'+str(temp3)+'\n')

fwrite.close()
print time.time()-t1