# coding: utf-8

import csv
import time

data_dir = "./data/"
result_dir = "./result/"
pic_dir = "./pic_Vien_shao5/"
city_dir = "./city/"


# 少了5张图片 遍历文件夹已下载的图片
import os

x = 1
for count in range(0, 34479):
    filePath = pic_dir + '%s.jpg' % x
    if os.path.exists(filePath):
        message = filePath + '\texists'
        print message
    else:
        message = '------------------------------------------------------'
        fwrite = open('./readme.txt', 'a+')
        fwrite.write(str(x) + '\t' + filePath + '\n')
        print message
    x += 1