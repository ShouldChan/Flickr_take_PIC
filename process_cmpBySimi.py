# coding:utf-8
import numpy as np
import time
import random
import operator

Toro_MAX_NUM = 100
Edin_MAX_NUM = 1000

t0 = time.time()
Edin_dict = {}
with open('./Edin_photoID_DESCRIPTION.txt','r') as fi_edin:
    lines = fi_edin.readlines()
    for line in lines:
        tempData = line.strip().split('\t')
        photo_id,jpg_name = tempData[0],tempData[1]
        Edin_dict[jpg_name] = photo_id
print 'read Edin_dict done...'

Toro_dict = {}
with open('./Toro_photoID_DESCRIPTION.txt','r') as fi_toro:
    lines = fi_toro.readlines()
    for line in lines:
        tempData = line.strip().split('\t')
        photo_id,jpg_name = tempData[0],tempData[1]
        Toro_dict[jpg_name] = photo_id
print 'read Toro_dict done...'

# 取Toro中的100张图片去Edin里遍历计算相似度
feat_Toro = {}

with open('./vector_Toro.txt','r') as fread:
    lines = fread.readlines()
    x = 0
    for line in lines:
        feat_Toro[x] = line
        x += 1
print 'read feat_Toro done...'

feat_Edin = {}

with open('./vector_Edin.txt','r') as fread:
    lines = fread.readlines()
    x = 0
    for line in lines:
        feat_Edin[x] = line
        x += 1
print 'read feat_Edin done...', time.time() - t0

# 思路一：将列表里的数据打乱 取前100个即可 和Edin比
# random.shuffle(feat_Toro)
# 思路二：取random数字 使用字典随机取
t1 = time.time()

simi_list = []
visits_Toro = set()
visits_Edin = set()

for iter_Toro in range(Toro_MAX_NUM):
    i_Toro = random.randint(0, 39301)

    while i_Toro in visits_Toro:
        i_Toro = random.randint(0, 39301)
    visits_Toro.add(i_Toro)

    print i_Toro
    mtx_i = np.matrix(feat_Toro[i_Toro])

    for iter_Edin in range(Edin_MAX_NUM):
        j_Edin = random.randint(0, 33865)

        while j_Edin in visits_Edin:
            j_Edin = random.randint(0, 33865)
        visits_Edin.add(j_Edin)

        mtx_j = np.matrix(feat_Edin[j_Edin])
        num = float(mtx_i * mtx_j.T)
        denom = np.linalg.norm(mtx_i) * np.linalg.norm(mtx_j)
        cos = num / denom
        sim = 0.5 + 0.5 * cos
        jpg_name_i = str(i_Toro + 1) + '.jpg'
        jpg_name_j = str(j_Edin + 1) + '.jpg'
        last_i = Toro_dict[jpg_name_i]
        last_j = Edin_dict[jpg_name_j]
        simi_list.append([last_i, last_j, sim])

print 'compute done...', time.time() - t1

simi_list.sort(key=operator.itemgetter(2),reverse=True)
print 'sort done...'

t2 = time.time()
fwrite = open('./Toro_TO_Edin_similarity.txt','a+')
for [last_i, last_j, sim] in simi_list:
    fwrite.write(str(last_i)+'\t'+str(last_j)+'\t'+str(sim)+'\n')
print 'write done...', time.time() - t2