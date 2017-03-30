# coding: utf-8

import csv
import time
from util import Util

data_dir = "./data/"
result_dir = "./result/"
pic_dir = "./pic/"
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

# 3.测试下载图片
# import requests

# with open(data_dir+'temp_data.txt', 'r') as frUrl:
#     # with open('E://test_yfcc100m_dataset.txt', 'r') as frUrl:
#     lines = frUrl.readlines()
#     photourllist_needtodownload = []
#     for line in lines:
#         tempData = line.strip().split('\t')
#         pho_id, urlData, isPhoto = tempData[2], tempData[16], tempData[24]
#         photourllist_needtodownload.append(urlData)
#         # print urlData + "\t" + isPhoto
#     # print photourllist_needtodownload
#     print "push ok"
#     x = 0
#     for photourl in photourllist_needtodownload:
#         rq = requests.get(photourl)
#         filePath = pic_dir + '%s.jpg' % x
#         x += 1
#         with open(filePath, 'wb') as picwrite:
#             picwrite.write(rq.content)

# 4.筛选后写个文件
# t = time.time()
# with open(result_dir + 'userVisits-Toro.txt','r') as fread:
# 	lines = fread.readlines()
# 	photo_list = []
# 	for eachline in lines:
# 		tempData = eachline.strip().split('\t')
# 		photo_id = tempData[0]
# 		photo_list.append(photo_id)
# 	print "push Toro_photoID list over:", time.time() - t
# with open(data_dir + 'yfcc100m_dataset.txt', 'r') as fread_yfcc:
# 	yfcc_lines = fread_yfcc.readlines()
# 	# photo_ntodl_list = []
# 	y = 0
# 	for yfcc_eachline in yfcc_lines:
# 		tempData = yfcc_eachline.strip().split('\t')
# 		pho_id, urlData, isPhoto = tempData[1], tempData[16], tempData[24]
# 		y += 1
# 		print y
# 		if pho_id in photo_list and isPhoto == '0' and urlData != '':
# 			x += 1
# 			print x
# 			with open(result_dir + 'Toro_photoID_url.txt', 'w+') as fwrite:
# 				fwrite.write(pho_id + '\t' + urlData + '\n')
# 	print "write Toro_photoID_url ok:", time.time() - t

# 5.将大文件取出自己需要的
# t = time.time()

# with open(data_dir + 'yfcc100m_dataset.txt', 'r') as fread_yfcc:
# 	yfcc_lines = fread_yfcc.readlines()
# 	count=0
# 	for yfcc_eachline in yfcc_lines:
# 		count+=1
# 		print count
# 		tempData = yfcc_eachline.strip().split('\t')
# 		pho_id, urlData, isPhoto = tempData[1], tempData[16], tempData[24]
# 		if isPhoto == '0':
# 			fwrite=open(data_dir+'photoID_url_dataset.txt','a+')
# 			fwrite.write(pho_id + '\t' + urlData + '\n')
# 	print "write Toro_photoID_url ok:", time.time() - t

# 6.按照取出需要的 把每个城市的url分类
# t1=time.time()

# photo_list = []

# with open(result_dir + 'userVisits-Buda-allPOI.txt','r') as fread_city:
# 	lines = fread_city.readlines()
# 	for eachline in lines:
# 		tempData = eachline.strip().split('\t')
# 		photo_id = tempData[0]
# 		photo_list.append(photo_id)

# # print photo_list
# print "push Buda_photoID list over:", time.time() - t1

# t2=time.time()

# with open(data_dir + 'photoID_url_dataset.txt','r') as fread_data:
# 	lines = fread_data.readlines()
# 	count=0
# 	for line in lines:
# 		count+=1
# 		print count
# 		tempData=line.strip().split('\t')
# 		pho_id, urlData = tempData[0], tempData[1]
# 		if pho_id in photo_list:
# 			fwrite_city=open(city_dir+'Buda_photoID_url.txt','a+')
# 			fwrite_city.write(pho_id + '\t' + urlData + '\n')
# 	print "write Buda_photoID_url ok:", time.time() - t2


# 7.下载图片！！！
# import requests


# def downloadPic(photourllist_needtodownload):
#     for photourl in photourllist_needtodownload:
#         rq = requests.get(photourl)
#         x = 0
#         filePath = pic_dir + '%s.jpg' % x
#         x += 1
#         with open(filePath, 'wb') as picwrite:
#             picwrite.write(rq.content)


# def readPhotoID():
#     with open(result_dir + 'userVisits-Toro.txt', 'r') as frpho:
#         lines = frpho.readlines()
#         phidList = []
#         for line in lines:
#             tempData = line.strip().split('\t')
#             photoid = tempData[0]
#             phidList.append(photoid)
#         return phidList


# def readUrl(phidList):
#     with open(data_dir+'yfcc100m_dataset.txt', 'r') as frUrl:
#         # with open('E://test_yfcc100m_dataset.txt', 'r') as frUrl:
#         lines = frUrl.readlines()
#         photourllist_needtodownload = []
#         y = 0
#         for line in lines:
#             tempData = line.strip().split('\t')
#             pho_id, urlData, isPhoto = tempData[2], tempData[16], tempData[24]
#             # print urlData + "\t" + isPhoto
#             x = 0
#             y += 1
#             print y
#             if isPhoto == '0' and pho_id in phidList:
#                 photourllist_needtodownload.append(urlData)
#                 x += 1
#                 print x
#     return photourllist_needtodownload


# def main():
#     t = time.time()
#     phidList = []
#     photourllist_needtodownload = ['http://farm5.staticflickr.com/4007/4436463882_b96a3d9df9.jpg','http://farm6.staticflickr.com/5468/9506922316_c19019e38f.jpg','http://farm3.staticflickr.com/2565/4140939180_07aeded917.jpg']
#     # readPhotoID()
#     # print "-----readPhotoID over-----"
#     # readUrl(phidList)
#     # print "-----readUrl over-----"
#     downloadPic(photourllist_needtodownload)
#     print "-----downloadPhoto over-----"
#     print time.time() - t


# if __name__ == '__main__':
#     main()

# 8.将大文件取出自己需要的
# t = time.time()

# with open(data_dir + 'yfcc100m_dataset.txt', 'r') as fread_yfcc:
# 	yfcc_lines = fread_yfcc.readlines()
# 	count=0
# 	for yfcc_eachline in yfcc_lines:
# 		count+=1
# 		print count
# 		tempData = yfcc_eachline.strip().split('\t')
# 		pho_id, isPhoto, lon, lat = tempData[1], tempData[24], tempData[12], tempData[13]
# 		if isPhoto == '0' and lon !='' and lat !='':
# 			fwrite=open(data_dir+'Geo_photoID_dataset.txt','a+')
# 			fwrite.write(str(pho_id) + '\t' + str(lon) + '\t' + str(lat) + '\n')
# 	print "write Toro_photoID_geo ok:", time.time() - t



# 9.get_geo we need, save the city's photo geo as txt

# t1=time.time()

# photo_list = []

# with open(result_dir + 'userVisits-Delh-allPOI.txt','r') as fread_city:
# 	lines = fread_city.readlines()
# 	for eachline in lines:
# 		tempData = eachline.strip().split('\t')
# 		photo_id = tempData[0]
# 		photo_list.append(photo_id)

# # print photo_list
# print "push Delh_photoID list over:", time.time() - t1

# t2=time.time()

# geo_list = []
# with open(data_dir + 'Geo_photoID_dataset.txt','r') as fread_data:
# 	lines = fread_data.readlines()
# 	count=0
# 	for line in lines:
# 		count+=1
# 		print count
# 		tempData=line.strip().split('\t')
# 		pho_id, lon, lat = tempData[0], tempData[1], tempData[2]
# 		if pho_id in photo_list:
# 			geo_list.append([pho_id,lon,lat])
# 			fwrite=open(data_dir+'Delh_Geo_dataset.txt','a+')
# 			fwrite.write(str(pho_id) + '\t' + str(lon) + '\t' + str(lat) + '\n')
# 	print "write Delh_photoID_geo ok:", time.time() - t2

# 10. Edin_Geo_preparation

# geo_dict = {}
# geo_list = []

# with open(data_dir + 'Delh_Geo_dataset.txt','r') as fread_data:
# 	lines = fread_data.readlines()
# 	count = 0
# 	for line in lines:
# 		count += 1
# 		# print count
# 		tempData = line.strip().split('\t')
# 		pho_id, lon, lat = tempData[0], tempData[1], tempData[2]
# 		geo_dict[pho_id] = lon+'\t'+lat
# 		geo_list.append(pho_id)
# 		# print geo_list


# t3=time.time()

# with open(result_dir + 'userVisits-Delh-allPOI.txt','r') as fread_city:
# 	lines = fread_city.readlines()
# 	# print type(lines)
# 	# print type(lines[0])
# 	for eachline in lines:
# 		tempData = eachline.strip().split('\t')
# 		pho_id, poiID, category, profit = tempData[0], tempData[3], tempData[4], tempData[5]
# 		# print str(geo_dict[pho_id])
# 		if pho_id in geo_list:
# 			fwrite = open(data_dir + 'Delh_Geo_preparation.txt','a+')
# 			fwrite.write(str(pho_id) + '\t' + str(geo_dict[pho_id])+ '\t' +str(poiID) + '\t' + str(category) + '\t' + str(profit)+ '\n')
# 	print "write Delh_Geo_preparation ok:", time.time() - t3

		


# 11. First, read userVisits 


# 11-1:poi_data: poiID, category, profit, lon, lat

# num_list = []
# with open(result_dir + 'userVisits-Delh-allPOI.txt','r') as fread_city:
# 	lines = fread_city.readlines()
# 	for eachline in lines:
# 		tempData = eachline.strip().split('\t')
# 		poiID = tempData[3]
# 		if poiID not in num_list:
# 			num_list.append(poiID)
# print len(num_list)


# 11-2:

# poi_data = set()
# num_list = []
# with open(data_dir + 'Delh_Geo_preparation.txt','r') as fread_city:
# 	lines = fread_city.readlines()
# 	for eachline in lines:
# 		tempData = eachline.strip().split('\t')
# 		poiID, lon, lat, category, profit = tempData[3], tempData[1], tempData[2], tempData[4], tempData[5]
# 		if poiID not in num_list:
# 			num_list.append(poiID)
# 			poi_data.add((poiID, lon, lat, category, profit))
# 			fwrite = open(data_dir + 'Delh_LAST_preparation.txt','a+')
# 			fwrite.write(str(poiID) + '\t' + str(lon)+ '\t' +str(lat) + '\t' + str(category) + '\t' + str(profit)+ '\n')
# print len(num_list)
# print poi_data

# 11-3:
def main():
	geo_dict = {}
	with open(data_dir + 'Delh_LAST_preparation.txt','r') as fread:
		lines = fread.readlines()
		for eachline in lines:
			tempData = eachline.strip().split('\t')
			poiID, lon, lat= int(tempData[0]), float(tempData[1]), float(tempData[2])
			geo_dict[poiID]=[lon,lat]

	print geo_dict

	poi_data = {}
	with open(data_dir + 'Delh_LAST_preparation.txt','r') as fread_city:
		lines = fread_city.readlines()
		for eachline in lines:
			tempData = eachline.strip().split('\t')
			poiID, lon, lat, category, profit = int(tempData[0]), tempData[1], tempData[2], tempData[3], tempData[4]
			poi_data[poiID] = profit+'\t'+category
	print poi_data

	t=time.time()

	for i in range(1,26):
		for j in range(1,26):
			if i!=j and i!=2 and j!=2 and i!=17 and j!=17 and i!=20 and j!=20:
				cost = util.dist(geo_dict[i],geo_dict[j])
				print cost
				fwrite = open(data_dir + 'Delh_COST_result.txt','a+')
				fwrite.write(str(i) + '\t' + str(j) + '\t'+str(cost)+'\t'+str(poi_data[j]) + '\n')

	print time.time()-t

if __name__ == '__main__':
	util = Util()
	main()