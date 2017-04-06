# coding:utf-8
import time
import operator

# here to change the city name, so u don't have to edit the codes below
CITY_NAME = 'Vien'

data_dir = "./data/"
result_dir = "./result/"
pic_dir = "./pic/"
city_dir = "./city/"
des_dir = "./des/"
hyb_dir = "./hybrid/"

# 读取POI点和对应的photoID
t1 = time.time()
pho_poi_dict = {}
with open(result_dir + 'userVisits-' + CITY_NAME + '.txt','r') as readPOI:
    lines = readPOI.readlines()
    for line in lines:
        tempData = line.strip().split('\t')
        photoID, poiID = tempData[0], tempData[3]
        # pho_poi_list.append([photoID, poiID])
        pho_poi_dict[photoID] = poiID
print 'read userVisits over: ', time.time()-t1

# 读取描述文件 photoID和文件名对应
t2 = time.time()
pho_jpg_list = []
with open(des_dir + CITY_NAME + '_photoID_DESCRIPTION.txt','r') as readDes:
    lines = readDes.readlines()
    for line in lines:
        tempData = line.strip().split('\t')
        photoID, jpgName = tempData[0], tempData[1]
        # pho_jpg_dict[photoID] = jpgName
        pho_jpg_list.append([photoID, jpgName])
print 'read Description over:', time.time() - t2

# 将所有获得的信息整合写入同一个文件
t3 = time.time()
hybrid_list = []

for [photoID, jpgName] in pho_jpg_list:
    poiID = int(pho_poi_dict[photoID])
    hybrid_list.append([photoID, jpgName, poiID])

hybrid_list.sort(key=operator.itemgetter(2),reverse=False)

fwrite = open(hyb_dir + CITY_NAME + '_Info_hybrid.txt','a+')
for [photoID, jpgName, poiID] in hybrid_list:
    fwrite.write(str(photoID)+'\t'+str(jpgName)+'\t'+str(poiID)+'\n')
fwrite.close()
print 'write over', time.time() - t3