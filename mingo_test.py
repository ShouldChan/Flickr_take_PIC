#!/usr/bin/python
#-*-coding:utf-8-*-

with open("/home/duncan/chenxiaojie","r") as f:
	lines = f.readlines()
	testdata = []
	data = []
	for line in lines:
		data = line.split("\t")
		value = []
		for d in data:
			if len(d) != 0:
				value.append(d.replace("\r\n",""))
		testdata.append(value)
with open("/home/duncan/top","r") as f:
	lines = f.readlines()
	top = []
	data = []
	for line in lines:
		data = line.split("\t")
		value = []
		for d in data:
			if len(d) != 0:
				value.append(d.replace("\n",""))
		top.append(value)
newTestData = []
for test in testdata:
	test = map(lambda x : int(x),test)
	newTestData.append(test)
newTopData = []

for t in top:
	test = map(lambda x : int(x),t)
	newTopData.append(test)
print len(newTopData),len(newTestData)
row = 0
count = 0
for test in testdata:
	for t in test:
		# print newTopData[row]
		if t in newTopData[row]:
			count += 1
	row += 1
print count