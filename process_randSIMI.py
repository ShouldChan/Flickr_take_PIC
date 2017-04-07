# coding:utf-8
import numpy as np
import time
CITY_NAME = 'Toro'

data_dir = "./data/"
result_dir = "./result/"
pic_dir = "./pic/"
city_dir = "./city/"
des_dir = "./des/"
hyb_dir = "./hybrid/"
rand_dir = "./random/"
vec_dir = "./vector/"
sim_dir = "./sim/"

t0 = time.time()
pho_jpg_dict = {}
pho_poi_dict = {}
vector_set = set()
with open(rand_dir + CITY_NAME + '_Random_list.txt','r') as fi:
    lines = fi.readlines()
    for line in lines:
        tempData = line.strip().split('\t')
        photoID, jpg_name, poiID = tempData[0], tempData[1], tempData[2]
        jpg_name_split = jpg_name.split('.')
        jpg_int = int(jpg_name_split[0])
        pho_jpg_dict[jpg_int] = photoID
        pho_poi_dict[photoID] = poiID
        vector_set.add(jpg_int)
print 'read image_dict done...', time.time() - t0

featAll = {}

with open(vec_dir + 'vector_'+ CITY_NAME +'.txt','r') as fread:
    lines = fread.readlines()
    x = 1
    for line in lines:
        # print x
        featAll[x] = line
        x += 1
print 'featAll done...', time.time() - t0

t1 = time.time()
simi_list = []

for iter_i in vector_set:
    mtx_i = np.matrix(featAll[iter_i])
    print iter_i
    for iter_j in vector_set: 
        if iter_i != iter_j:
            mtx_j = np.matrix(featAll[iter_j])
            num = float(mtx_i * mtx_j.T)
            denom = np.linalg.norm(mtx_i) * np.linalg.norm(mtx_j)
            cos = num / denom
            sim = 0.5 + 0.5 * cos
            photoID_i = pho_jpg_dict[iter_i]
            photoID_j = pho_jpg_dict[iter_j]
            simi_list.append([photoID_i, photoID_j, sim])

print 'compute done...', time.time() - t1

t2 = time.time()
fwrite = open(sim_dir + CITY_NAME +'_Rand_SIMI.txt','a+')
for [photoID_i, photoID_j, sim] in simi_list:
    fwrite.write(str(photoID_i)+'\t'+str(photoID_j)+'\t'+str(sim)+'\n')
print 'write done...', time.time() - t2