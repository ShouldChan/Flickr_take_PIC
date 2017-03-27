# coding: utf-8

import csv
import time

data_dir = "./data/"
result_dir = "./result/"
pic_dir = "./pic_Edin/"
city_dir = "./city/"

# 1.将这个以；保存的非标准csv转为txt,读出每一列值并存入list，再写入
# with open(data_dir + "userVisits-Vien-allPOI.csv") as csvfile:
#     # lines = csv.DictReader(csvfile)
#     lines = csvfile.readlines()
#     # all_data = []
#     txt_write = open(result_dir + "userVisits-Vien-allPOI.txt", "w")
#     for line in lines:
#         data = line.strip().split(";")
#         photoID, userID_f, dateTaken, poiID, poiTheme_f, poiFreq, seqID = data[0], data[1], data[2], data[3], data[4], \
#                                                                           data[5], data[6]
#         userID = userID_f.strip('"')
#         poiTheme = poiTheme_f.strip('"')
#         # all_data.append([photoID, userID, dateTaken, poiID, poiTheme, poiFreq, seqID])
#         txt_write.write(
#             photoID + "\t" + userID + "\t" + dateTaken + "\t" + poiID + "\t" + poiTheme + "\t" + poiFreq + "\t" + seqID + "\n" )
#         # print userID

# 2.根据url下载图片test
# import requests
# # 下载图片
# def dowloadPic(imageUrl,filePath):
#     r = requests.get(imageUrl)
#     with open(filePath, "wb") as code:
#         code.write(r.content)
#
# url = 'http://farm8.staticflickr.com/7231/7289030198_1f1ba44113.jpg'
# filePath = "E://1.jpg"
# dowloadPic(url,filePath)

# 3.测试集测试下图片
# import requests
#
# with open('E://temp_data.txt', 'r') as frUrl:
#     # with open('E://test_yfcc100m_dataset.txt', 'r') as frUrl:
#     lines = frUrl.readlines()
#     photourllist_needtodownload = []
#     for line in lines:
#         tempData = line.strip().split('\t')
#         pho_id, urlData, isPhoto = tempData[2], tempData[16], tempData[24]
#         photourllist_needtodownload.append(urlData)
#         # print urlData + "\t" + isPhoto
#     # print photourllist_needtodownload
#     x = 0
#     for photourl in photourllist_needtodownload:
#         rq = requests.get(photourl)
#         filePath = 'E://pic//%s.jpg' % x
#         x += 1
#         with open(filePath, 'wb') as picwrite:
#             picwrite.write(rq.content)

# 4.下载图片！！！
# import requests
#
#
# def downloadPic(photourllist_needtodownload):
#     for photourl in photourllist_needtodownload:
#         rq = requests.get(photourl)
#         x = 0
#         filePath = 'E://%s.jpg' % x
#         x += 1
#         with open(filePath, 'wb') as picwrite:
#             picwrite.write(rq.content)
#
#
# def readPhotoID():
#     with open(result_dir + 'userVisits-Toro.txt', 'r') as frpho:
#         lines = frpho.readlines()
#         phidList = []
#         for line in lines:
#             tempData = line.strip().split('\t')
#             photoid = tempData[0]
#             phidList.append(photoid)
#         return phidList
#
#
# def readUrl(phidList):
#     with open('E://yfcc100m//yfcc100m_dataset//yfcc100m_dataset.txt', 'r') as frUrl:
#         # with open('E://test_yfcc100m_dataset.txt', 'r') as frUrl:
#         lines = frUrl.readlines()
#         photourllist_needtodownload = []
#         for line in lines:
#             tempData = line.strip().split('\t')
#             pho_id, urlData, isPhoto = tempData[2], [16], tempData[24]
#             # print urlData + "\t" + isPhoto
#             x = 0
#             if isPhoto == '0' and pho_id in phidList:
#                 photourllist_needtodownload.append(urlData)
#                 x += 1
#                 print x
#     return photourllist_needtodownload
#
#
# def main():
#     t = time.time()
#     phidList = []
#     photourllist_needtodownload = []
#     readPhotoID()
#     print "-----readPhotoID over-----"
#     readUrl(phidList)
#     print "-----readUrl over-----"
#     downloadPic(photourllist_needtodownload)
#     print "-----downloadPhoto over-----"
#     print time.time() - t
#
#
# if __name__ == '__main__':
#     main()
# 5.多进程操作
# import os
# import threading
#
# mutex = threading.Lock()
# fp = open('E://temp_data.txt', 'r')
#
#
# class Reader(threading.Thread):
#     def __init__(self, num):
#         # super().__init__()
#         self.num = num
#
#     def run(self):
#         while True:
#             with mutex:
#                 line = fp.readline()
#                 if len(line) == 0:
#                     return
#                 print('%d:%s' % (self.num, line))
#                 time.sleep(0.1)
#
#
# if __name__ == "__main__":
#     r1 = Reader(1)
#     r2 = Reader(2)
#     r1.start()
#     r2.start()
#
#     r1.join()
#     r2.join()

# import os, time
# import threading
#
# rlock = threading.RLock()
# curPosition = 0
#
#
# def push_photoList(photo_list):
#     t = time.time()
#     with open(result_dir + 'userVisits-Glas.txt', 'r') as fread:
#         lines = fread.readlines()
#         for eachline in lines:
#             tempData = eachline.strip().split('\t')
#             photo_id = tempData[0]
#             photo_list.append(photo_id)
#         print "push Glas_photoID list over:", time.time() - t
#
#
# class Reader(threading.Thread):
#     def __init__(self, res):
#         self.res = res
#         super(Reader, self).__init__()
#
#     def run(self):
#         global curPosition
#         fstream = open(self.res.fileName, 'r')
#         while True:
#             # 锁定共享资源
#             rlock.acquire()
#             startPosition = curPosition
#             curPosition = endPosition = (startPosition + self.res.blockSize) if (
#                                                                                 startPosition + self.res.blockSize) < self.res.fileSize else self.res.fileSize
#             # 释放共享资源
#             rlock.release()
#             if startPosition == self.res.fileSize:
#                 break
#             elif startPosition != 0:
#                 fstream.seek(startPosition)
#                 fstream.readline()
#             pos = fstream.tell()
#             while pos < endPosition:
#                 yfcc_eachline = fstream.readline()
#                 # 处理line
#                 # for yfcc_eachline in yfcc_lines:
#                 tempData = yfcc_eachline.strip().split('\t')
#                 pho_id, urlData, isPhoto = tempData[2], tempData[16], tempData[24]
#                 print urlData
#                 if pho_id in photo_list and isPhoto == '0' and urlData != '':
#                     print 1
#                     with open(result_dir + 'Glas_photoID_url.txt', 'wb') as fwrite:
#                         fwrite.write(pho_id + '\t' + urlData + '\n')
#             # print(line.strip())
#             pos = fstream.tell()
#
#         fstream.close()
#
#
# class Resource(object):
#     def __init__(self, fileName):
#         self.fileName = fileName
#         # 分块大小
#         self.blockSize = 100000000
#         self.getFileSize()
#
#     # 计算文件大小
#     def getFileSize(self):
#         fstream = open(self.fileName, 'r')
#         fstream.seek(0, os.SEEK_END)
#         self.fileSize = fstream.tell()
#         fstream.close()
#
#
# if __name__ == '__main__':
#     photo_list = []
#     starttime = time.clock()
#     # 线程数
#     threadNum = 4
#     # 文件
#     fileName = 'E://temp_data.txt';
#     res = Resource(fileName)
#     threads = []
#     # 初始化线程
#     for i in range(threadNum):
#         rdr = Reader(res)
#         threads.append(rdr)
#     # 开始线程
#     for i in range(threadNum):
#         threads[i].start()
#     # 结束线程
#     for i in range(threadNum):
#         threads[i].join()
#
#     print(time.clock() - starttime)

# 5. 测试多进程
# import multiprocessing
#
# t0 = time.time()
#
# with open(result_dir + 'Toro_photoID_url.txt', 'r') as frpho:
#     lines = frpho.readlines()
#     phidList = []
#     for line in lines:
#         tempData = line.strip().split('\t')
#         photo_url = tempData[1]
#         phidList.append(photo_url)
#
# # print phidList
# print 'readPhotoID elapsed:', time.time() - t0
#
# t1 = time.time()
#
#
# def read_dataset(start, end):
#     fopen = open('E://temp_data.txt', 'r')
#     result_list = []
#     lines = fopen.readlines()[start:end]
#     for eachline in lines:
#         tempData = eachline.strip().split('\t')
#         pho_id, urlData, isPhoto = tempData[1], tempData[16], tempData[24]
#         if pho_id in phidList and isPhoto == '0' and urlData != '':
#             result_list.append([pho_id, urlData])
#             # with open(result_dir + 'Toro_photoID_url.txt', 'wb') as fwrite:
#             #     fwrite.write(pho_id + '\t' + urlData + '\n')
#     return result_list


# read_dataset(0, 23712)
# print 'write photoID_url elapsed:', time.time() - t1

# pool = multiprocessing.Pool(processes=4)
#
# t2 = time.time()
# s = 0
# e = 0
# for i in range(0, 4):
#     s = e
#     e = s + 5928
#     res = pool.apply_async(read_dataset, (s, e))
# pool.close()
# pool.join()
#
# print 'muliwrite photoID_url elapsed:', time.time() - t2

# 4.下载图片！！！
import requests

t = time.time()


def downloadPic(photourllist_needtodownload):
    x = 0
    for photourl in photourllist_needtodownload:
        x += 1
        print x
        filePath_txt = pic_dir + '%s.txt' % x
        print  photourl
        try:
            rq = requests.get(photourl, timeout=60)
        except requests.exceptions.ConnectionError:
            print 'md!超时了！'
            fwrite = open(filePath_txt, 'w')
            fwrite.write(str(photourl))
            print '-------------------------------------------------------------------------------------------'
            continue
        filePath_pic = pic_dir + '%s.jpg' % x

        with open(filePath_pic, 'wb') as picwrite:
            picwrite.write(rq.content)
        print time.time() - t
        print '----------------------------------------'


def readUrl(photourllist_needtodownload):
    with open(city_dir + 'Edin_photoID_url.txt', 'r') as frpho:
        lines = frpho.readlines()
        count = 0
        for line in lines:
            count += 1
            tempData = line.strip().split('\t')
            photo_url = tempData[1]
            photourllist_needtodownload.append(photo_url)


def main():
    photourllist_needtodownload = []
    readUrl(photourllist_needtodownload)
    # print photourllist_needtodownload
    print "-----readUrl over-----"
    downloadPic(photourllist_needtodownload)
    print "-----downloadPhoto over-----"


if __name__ == '__main__':
    main()
