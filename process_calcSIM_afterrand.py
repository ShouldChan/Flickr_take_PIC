import numpy as np
import time

CITY_NAME = 'Buda'
data_dir = "./data/"
result_dir = "./result/"
pic_dir = "./pic/"
city_dir = "./city/"
des_dir = "./des/"
hyb_dir = "./hybrid/"
rand_dir = "./random/"
lost_dir = "./lost/"
vector_dir = './vector/'
ran_sim_dir = './sim/'

t0 = time.time()
image_dict = {}
with open(des_dir + CITY_NAME + '_photoID_DESCRIPTION.txt','r') as fi:
    lines = fi.readlines()
    for line in lines:
        tempData = line.strip().split('\t')
        photo_id,jpg_name = tempData[0],tempData[1]
        image_dict[photo_id] = jpg_name
print 'read image_dict done...'


t2 = time.time()
fwrite = open(ran_sim_dir + CITY_NAME + '_rand_similarity.txt','a+')

with open(ran_sim_dir + CITY_NAME + '_Rand_SIMI.txt','r') as fii:
    lines = fii.readlines()
    for line in lines:
        tempData = line.strip().split('\t')
        photoID_1,poiID_1,photoID_2,poiID_2,sim_1_2 = tempData[0],tempData[1],tempData[2],tempData[3],tempData[4]
        fwrite.write(str(image_dict[photoID_1])+'\t'+str(image_dict[photoID_2])+'\t'+sim_1_2+'\n')

print 'write done...', time.time() - t2
