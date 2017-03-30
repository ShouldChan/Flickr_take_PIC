# coding: utf-8

import csv
import time

data_dir = "./data/"
result_dir = "./result/"
pic_dir = "./pic/"
city_dir = "./city/"
csv_dir = "./csv/"
cost_dir = "./cost/"

# csvfile = file(csv_dir + 'csvtest.csv', 'wb')
# writer = csv.writer(csvfile)
# writer.writerow(['id', 'url', 'keywords'])
# data = [
#   ('1', 'http://www.xiaoheiseo.com/', '小黑'),
#   ('2', 'http://www.baidu.com/', '百度'),
#   ('3', 'http://www.jd.com/', '京东')
# ]
# writer.writerows(data)
# csvfile.close()

data = []
with open(cost_dir + 'Pert_COST_result.txt','r') as fread_Osak:
	lines = fread_Osak.readlines()
	for line in lines:
		tempData = line.strip().split('\t')
		s_from,s_to,s_cost,s_profit,s_category = tempData[0],tempData[1],tempData[2],tempData[3],tempData[4]
		data.append((s_from,s_to,s_cost,s_profit,s_category))
	csvfile = file(csv_dir + 'Pert_COST_result.csv', 'wb')
	writer = csv.writer(csvfile)
	writer.writerow(['from', 'to', 'cost','profit','category'])
	writer.writerows(data)
	csvfile.close()