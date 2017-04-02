import numpy as np

# caocao=np.load('./1.npy')
# pengpeng=np.load('./2.npy')

# num=float(caocao.T * pengpeng)
# denom=np.linalg.norm(caocao)*linalg.norm(pengpeng)
# cos=num/denom
# sim=0.5+0.5*cos
# print sim

# with open('./1.txt','r') as fread:
# 	lines=fread.readlines()
# 	for line in lines:
# 		mtx=np.matrix(line)
# 		print mtx

# mtx=np.loadtxt(open('./1.txt','rb'))
# print mtx

image_dict = {}
with open('./Edin_photoID_DESCRIPTION.txt','r') as fi:
    lines = fi.readlines()
    for line in lines:
        tempData = line.strip().split('\t')
        photo_id,jpg_name = tempData[0],tempData[1]
        image_dict[jpg_name] = photo_id
print 'read image_dict done...'

featAll = []

with open('./vector_Edin.txt','r') as fread:
	lines = fread.readlines()
	x = 1
	for line in lines:
		# print x
		x += 1
		featAll.append(line)
print 'featAll done...'

i = 1
for line_i in featAll:
    mtx_i = np.matrix(line_i)
    j = 1
    for line_j in featAll: 
    # print line
        if i != j:
            mtx_j = np.matrix(line_j)
            num = float(mtx_i * mtx_j.T)
            denom = np.linalg.norm(mtx_i) * np.linalg.norm(mtx_j)
            cos = num / denom
            sim = 0.5 + 0.5 * cos
            fwrite = open('./Edin_similarity','a+')
            jpg_name_i = str(i) + '.jpg'
            jpg_name_j = str(j) + '.jpg'
            fwrite.write(str(image_dict[jpg_name_i])+'\t'+str(image_dict[jpg_name_j])+'\t'+str(sim)+'\n')
            print i,'->',j,'----',sim
    	j += 1
    i += 1