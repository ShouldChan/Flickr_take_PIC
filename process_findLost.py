# coding: utf-8

# 剔除无效图片
import os

CITY_NAME = 'Edin'
MAX_NUM = 33866

pic_dir = './pic_' + CITY_NAME + '/'

fwrite = open('./' + CITY_NAME + '_LOST.txt', 'a+')
for x in range(1, MAX_NUM):
    filePath = pic_dir + '%s.jpg' % x
    if os.path.isfile(filePath):
        print 'yep!'
    else:
        fwrite.write(str(x) + '\n')
        print 'no!'