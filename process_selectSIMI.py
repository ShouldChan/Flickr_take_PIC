# coding: utf-8

import csv
import time
import operator

data_dir = "./data/"
result_dir = "./result/"
pic_dir = "./pic/"
city_dir = "./city/"
simi_dir = "./similarity/"

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
#   lines = fread.readlines()
#   photo_list = []
#   for eachline in lines:
#       tempData = eachline.strip().split('\t')
#       photo_id = tempData[0]
#       photo_list.append(photo_id)
#   print "push Toro_photoID list over:", time.time() - t
# with open(data_dir + 'yfcc100m_dataset.txt', 'r') as fread_yfcc:
#   yfcc_lines = fread_yfcc.readlines()
#   # photo_ntodl_list = []
#   y = 0
#   for yfcc_eachline in yfcc_lines:
#       tempData = yfcc_eachline.strip().split('\t')
#       pho_id, urlData, isPhoto = tempData[1], tempData[16], tempData[24]
#       y += 1
#       print y
#       if pho_id in photo_list and isPhoto == '0' and urlData != '':
#           x += 1
#           print x
#           with open(result_dir + 'Toro_photoID_url.txt', 'w+') as fwrite:
#               fwrite.write(pho_id + '\t' + urlData + '\n')
#   print "write Toro_photoID_url ok:", time.time() - t

# 5.将大文件取出自己需要的
# t = time.time()

# with open(data_dir + 'yfcc100m_dataset.txt', 'r') as fread_yfcc:
#   yfcc_lines = fread_yfcc.readlines()
#   count=0
#   for yfcc_eachline in yfcc_lines:
#       count+=1
#       print count
#       tempData = yfcc_eachline.strip().split('\t')
#       pho_id, urlData, isPhoto = tempData[1], tempData[16], tempData[24]
#       if isPhoto == '0':
#           fwrite=open(data_dir+'photoID_url_dataset.txt','a+')
#           fwrite.write(pho_id + '\t' + urlData + '\n')
#   print "write Toro_photoID_url ok:", time.time() - t

# 6.按照取出需要的 把每个城市的url分类
# t1=time.time()

# photo_list = []

# with open(result_dir + 'userVisits-Pert-allPOI.txt','r') as fread_city:
#     lines = fread_city.readlines()
#     for eachline in lines:
#         tempData = eachline.strip().split('\t')
#         photo_id = tempData[0]
#         photo_list.append(photo_id)

# # print photo_list
# print "push Pert_photoID list over:", time.time() - t1

# t2=time.time()

# with open(data_dir + 'photoID_url_dataset.txt','r') as fread_data:
#     lines = fread_data.readlines()
#     count=0
#     for line in lines:
#         count+=1
#         print count
#         tempData=line.strip().split('\t')
#         pho_id, urlData = tempData[0], tempData[1]
#         if pho_id in photo_list:
#             fwrite_city=open(city_dir+'Pert_photoID_url.txt','a+')
#             fwrite_city.write(pho_id + '\t' + urlData + '\n')
#     print "write Pert_photoID_url ok:", time.time() - t2


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

# 8.附加任务 图片ID对应图片文件名
# t1=time.time()
# with open(city_dir+'Toro_photoID_url.txt','r') as fread_Toro:
# 	lines=fread_Toro.readlines()
# 	count=1
# 	for line in lines:
# 		tempData=line.strip().split('\t')
# 		photoID=tempData[0]
# 		pic_location=str(count)+'.jpg'
# 		print pic_location
# 		count+=1
# 		fwrite_Toro=open(city_dir+'Toro_photoID_DESCRIPTION.txt','a+')
# 		fwrite_Toro.write(str(photoID)+'\t'+str(pic_location)+'\n')
# print time.time()-t1

# t2=time.time()
# with open(city_dir+'Edin_photoID_url.txt','r') as fread_Toro:
# 	lines=fread_Toro.readlines()
# 	count=1
# 	for line in lines:
# 		tempData=line.strip().split('\t')
# 		photoID=tempData[0]
# 		pic_location=str(count)+'.jpg'
# 		print pic_location
# 		count+=1
# 		fwrite_Toro=open(city_dir+'Edin_photoID_DESCRIPTION.txt','a+')
# 		fwrite_Toro.write(str(photoID)+'\t'+str(pic_location)+'\n')
# print time.time()-t2

# t3=time.time()
# with open(city_dir+'Glas_photoID_url.txt','r') as fread_Toro:
# 	lines=fread_Toro.readlines()
# 	count=1
# 	for line in lines:
# 		tempData=line.strip().split('\t')
# 		photoID=tempData[0]
# 		pic_location=str(count)+'.jpg'
# 		print pic_location
# 		count+=1
# 		fwrite_Toro=open(city_dir+'Glas_photoID_DESCRIPTION.txt','a+')
# 		fwrite_Toro.write(str(photoID)+'\t'+str(pic_location)+'\n')
# print time.time()-t3

# t4=time.time()
# with open(city_dir+'Osak_photoID_url.txt','r') as fread_Toro:
# 	lines=fread_Toro.readlines()
# 	count=1
# 	for line in lines:
# 		tempData=line.strip().split('\t')
# 		photoID=tempData[0]
# 		pic_location=str(count)+'.jpg'
# 		print pic_location
# 		count+=1
# 		fwrite_Toro=open(city_dir+'Osak_photoID_DESCRIPTION.txt','a+')
# 		fwrite_Toro.write(str(photoID)+'\t'+str(pic_location)+'\n')
# print time.time()-t4

# 10.根据CNN分析出的图片相似度 选取四对不同类别相似的图片 和 四对同类别相似的图片
# 首先将图片ID和分类对号入座
pic_cate_dict = {}
pic_poi_dict = {}
with open(result_dir + 'userVisits-Osak.txt','r') as fread_result:
	lines = fread_result.readlines()
	for line in lines:
		tempData = line.strip().split('\t')
		photoID, poiID, category = tempData[0], tempData[3], tempData[4]
		pic_cate_dict[photoID] = category
		pic_poi_dict[photoID] = poiID

print 'pic_cate_dict, pic_poi_dict   ok...'
# 读取图片ID和文件名对应
pic_loc_dict = {}
with open(city_dir+'Osak_photoID_DESCRIPTION.txt','r') as fread_loc:
	lines = fread_loc.readlines()
	for line in lines:
		tempData = line.strip().split('\t')
		pic_id, pic_loc = tempData[0], tempData[1]
		pic_loc_dict[pic_id] = pic_loc

print 'pic_loc_dict   ok...'
# 根据相似度高低排列降序排列，除去相似度为1的失效图片 和 同一个POI点的图片不算
simi_list = []
with open(simi_dir + 'Osak_similarity.txt','r') as fread_simi:
	lines = fread_simi.readlines()
	for line in lines:
		tempData = line.strip().split('\t')
		p_from, p_to, simi = tempData[0], tempData[1], tempData[2]
		simi_list.append([p_from, p_to, simi])

print 'simi_list   ok...'

simi_list.sort(key=operator.itemgetter(2),reverse=True)

print 'sort: simi_list   ok...'

# 对排列好的筛选合适的图片 并输出他们的图片ID和文件名
for [p_from, p_to, simi] in simi_list:
	print 'Entering'
	poi_Issame = pic_poi_dict[p_from] == pic_poi_dict[p_to]
	cate_Issame = pic_cate_dict[p_from] == pic_cate_dict[p_to]
	if simi != '1.0' and poi_Issame == False and cate_Issame == True:
		fwrite = open(simi_dir+'Osak_SIMI_PIC.txt','a+')
		fwrite.write(str(pic_loc_dict[p_from])+'\t'+str(pic_loc_dict[p_to])+'\t'+str(simi)+'\n')
print 'Not the same cate: ok...'

for [p_from, p_to, simi] in simi_list:
	print 'Entering'
	poi_Issame = pic_poi_dict[p_from] == pic_poi_dict[p_to]
	cate_Issame = pic_cate_dict[p_from] == pic_cate_dict[p_to]
	if simi != '1.0' and poi_Issame == False and cate_Issame == False:
		fwrite = open(simi_dir+'Osak_SIMI_PIC.txt','a+')
		fwrite.write(str(pic_loc_dict[p_from])+'\t'+str(pic_loc_dict[p_to])+'\t'+str(simi)+'\n')
print 'The same cate: ok...'