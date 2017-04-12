# coding:utf-8
import time
import operator
import random

# here to change the city name, so u don't have to edit the codes below
CITY_NAME = 'Toronto'

data_dir = "./data/"
result_dir = "./result/"
pic_dir = "./pic/"
city_dir = "./city/"
des_dir = "./des/"
hyb_dir = "./hybrid/"
rand_dir = "./random/"
lost_dir = "./lost/"
place_dir = "./places/"

# yfcc100m_places
t0 = time.time()


global Toro_num, Osak_num, Glas_num, Edin_num, Pert_num, Buda_num, Delh_num, Vien_num

Toro_num = Osak_num = Glas_num = Edin_num = Pert_num = Buda_num = Delh_num = Vien_num = 0

# 不算空行
with open(data_dir + 'yfcc100m_places.txt', 'r') as readCity:
    lines = readCity.readlines()
    print type(lines)
    for i in range(0, len(lines)):
        temp = lines[i]
        print i

        if temp.find('Toronto') != -1:
            Toro_num += 1
            continue
        elif temp.find('Osaka') != -1:
            Osak_num += 1
            continue
        elif temp.find('Glasgow') != -1:
            Glas_num += 1
            continue
        elif temp.find('Edinburgh') != -1:
            Edin_num += 1
            continue
        elif temp.find('Perth') != -1:
            Pert_num += 1
            continue
        elif temp.find('Budapest') != -1:
            Buda_num += 1
            continue
        elif temp.find('Delhi') != -1:
            Delh_num += 1
            continue
        elif temp.find('Vienna') != -1:
            Vien_num += 1
            continue
        else:
            continue

print 'count Toro_num: \t %d \tok:\t' % Toro_num, time.time() - t0
print 'count Osak_num: \t %d \tok:\t' % Osak_num, time.time() - t0
print 'count Glas_num: \t %d \tok:\t' % Glas_num, time.time() - t0
print 'count Edin_num: \t %d \tok:\t' % Edin_num, time.time() - t0
print 'count Pert_num: \t %d \tok:\t' % Pert_num, time.time() - t0
print 'count Buda_num: \t %d \tok:\t' % Buda_num, time.time() - t0
print 'count Delh_num: \t %d \tok:\t' % Delh_num, time.time() - t0
print 'count Vien_num: \t %d \tok:\t' % Vien_num, time.time() - t0

with open(place_dir + 'city_num.txt','a+') as writeCity:
    writeCity.write('count Toro_num: ' + str(Toro_num)+'\n')
    writeCity.write('count Osak_num: ' + str(Osak_num)+'\n')
    writeCity.write('count Glas_num: ' + str(Glas_num)+'\n')
    writeCity.write('count Edin_num: ' + str(Edin_num)+'\n')
    writeCity.write('count Pert_num: ' + str(Pert_num)+'\n')
    writeCity.write('count Buda_num: ' + str(Buda_num)+'\n')
    writeCity.write('count Delh_num: ' + str(Delh_num)+'\n')
    writeCity.write('count Vien_num: ' + str(Vien_num)+'\n')


# # 算空行
# global city_num
# global flag

# city_num = 0
# flag = 0
# with open(data_dir + 'yfcc100m_places.txt', 'r') as readCity:
#     lines = readCity.readlines()
#     print type(lines)
#     l = 0
#     for i in range(0, len(lines)):
#         temp = lines[i]
#         l = len(temp)
#         print l
#         if l >= 20:
#             if temp.find(CITY_NAME) != -1:
#                 city_num += 1
#                 # print 'ok'
#                 flag = 1
#                 continue
#             else:
#                 flag = 0
#                 continue
#         elif flag == 1 and l < 20:
#             city_num += 1

# print 'count city_num: \t %d \tok:\t' % city_num, time.time() - t0
# with open(place_dir + CITY_NAME + '_places.txt','wb') as writeCity:
#     writeCity.write('count city_num: ' + str(city_num))